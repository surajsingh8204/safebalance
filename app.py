from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.preprocessing import RobustScaler
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

# Load the trained model
model = XGBClassifier()
model.load_model('xgb_final_model.json')

# Get the feature names the model expects
try:
    expected_features = model.get_booster().feature_names
    print(f"Model expects these features: {expected_features}")
except:
    expected_features = None
    print("Could not get feature names from model")

# Global scaler (will be fitted on reference data)
scaler = RobustScaler()

# Reference training data statistics for preprocessing
# These values come from your training data (df8)
REFERENCE_STATS = {}

def preprocess_input(data):
    """
    Preprocess input data following the exact same pipeline as training
    """
    # Create DataFrame from input
    df = pd.DataFrame([data])
    
    # Handle fyear - use user input or default
    if 'fyear' not in df.columns or pd.isna(df['fyear'].iloc[0]) or df['fyear'].iloc[0] == '':
        df['fyear'] = 2020.0
    else:
        df['fyear'] = float(df['fyear'].iloc[0])
    
    # Step 1: One-hot encode Division
    division_cols = ['Division_B', 'Division_C', 'Division_D', 'Division_E', 
                     'Division_F', 'Division_G', 'Division_H', 'Division_I']
    
    for col in division_cols:
        df[col] = 0
    
    if 'Division' in data and data['Division'] != 'A' and data['Division'] != 'J':
        div_col = f"Division_{data['Division']}"
        if div_col in division_cols:
            df[div_col] = 1
    
    if 'Division' in df.columns:
        df = df.drop(columns=['Division'])
    
    # Step 2: MajorGroup frequency encoding
    major_group_freq_map = {
        '50': 8000, '51': 7500, '73': 6000, '36': 5500, '35': 5000,
        '38': 4500, '49': 4000, '59': 3500, '34': 3000, '58': 2800,
        '20': 2500, '37': 2200, 'Other': 500
    }
    
    if 'MajorGroup' in data:
        mg = str(data['MajorGroup'])
        df['MajorGroup_freq'] = major_group_freq_map.get(mg, major_group_freq_map['Other'])
    else:
        df['MajorGroup_freq'] = 500
    
    if 'MajorGroup' in df.columns:
        df = df.drop(columns=['MajorGroup'])
    
    # Step 3: Feature Engineering - Create financial ratios
    eps = 1e-6
    df['Leverage_Ratio'] = df['X18'] / (df['X10'] + eps)
    df['Current_Ratio'] = df['X1'] / (df['X14'] + eps)
    df['Profit_Margin'] = df['X6'] / (df['X17'] + eps)
    df['Asset_Turnover'] = df['X17'] / (df['X10'] + eps)
    df['Debt_to_Equity'] = df['X18'] / (df['X10'] - df['X18'] + eps)
    df['EBIT_Margin'] = df['X11'] / (df['X17'] + eps)
    df['Gross_Margin'] = df['X13'] / (df['X17'] + eps)
    df['Receivables_Ratio'] = df['X7'] / (df['X10'] + eps)
    df['Inventory_Turnover'] = df['X2'] / (df['X5'] + eps)
    
    # Step 4: Log transformation on ratio features
    ratio_features = [
        'Leverage_Ratio', 'Current_Ratio', 'Profit_Margin',
        'Asset_Turnover', 'EBIT_Margin', 'Gross_Margin',
        'Receivables_Ratio', 'Inventory_Turnover'
    ]
    
    for col in ratio_features:
        if col in df.columns:
            df[col] = np.sign(df[col]) * np.log1p(np.abs(df[col]))
    
    # Step 5: Simple normalization (no fitting needed)
    # Just ensure values are in reasonable range
    numeric_features = [col for col in df.columns if col.startswith("X")]
    
    # Ensure column order matches training - MODEL EXPECTS fyear FIRST!
    expected_cols = ['fyear', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10',
                     'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18',
                     'Division_B', 'Division_C', 'Division_D', 'Division_E',
                     'Division_F', 'Division_G', 'Division_H', 'Division_I',
                     'MajorGroup_freq', 'Leverage_Ratio', 'Current_Ratio',
                     'Profit_Margin', 'Asset_Turnover', 'Debt_to_Equity',
                     'EBIT_Margin', 'Gross_Margin', 'Receivables_Ratio',
                     'Inventory_Turnover']
    
    # Add missing columns with default values
    for col in expected_cols:
        if col not in df.columns:
            if col == 'fyear':
                df[col] = 2020.0  # Default year
            else:
                df[col] = 0
    
    # Reorder columns
    df = df[expected_cols]
    
    return df

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Validate required fields
        required_fields = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10',
                          'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18']
        
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Preprocess the input
        processed_data = preprocess_input(data)
        
        # Make prediction
        probability = float(model.predict_proba(processed_data)[0][1])
        
        # Apply threshold (same as training: 0.35)
        threshold = 0.35
        prediction = 'Failed' if probability >= threshold else 'Alive'
        
        # Calculate risk score (0-100)
        risk_score = int(probability * 100)
        
        # Risk category
        if risk_score < 20:
            risk_category = 'Very Low Risk'
        elif risk_score < 35:
            risk_category = 'Low Risk'
        elif risk_score < 50:
            risk_category = 'Moderate Risk'
        elif risk_score < 70:
            risk_category = 'High Risk'
        else:
            risk_category = 'Very High Risk'
        
        return jsonify({
            'prediction': str(prediction),
            'probability': float(round(probability, 4)),
            'risk_score': int(risk_score),
            'risk_category': str(risk_category),
            'threshold': float(threshold)
        })
    
    except Exception as e:
        print(f"Error in prediction: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'model': 'loaded'})

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """Endpoint for batch predictions from CSV"""
    try:
        data = request.json
        companies = data.get('companies', [])
        
        if not companies:
            return jsonify({'error': 'No companies provided'}), 400
        
        results = []
        for company in companies:
            try:
                processed_data = preprocess_input(company)
                probability = model.predict_proba(processed_data)[0][1]
                prediction = 'Failed' if probability >= 0.35 else 'Alive'
                
                results.append({
                    'company_name': company.get('company_name', 'Unknown'),
                    'prediction': prediction,
                    'probability': round(probability, 4),
                    'risk_score': int(probability * 100)
                })
            except Exception as e:
                results.append({
                    'company_name': company.get('company_name', 'Unknown'),
                    'error': str(e)
                })
        
        return jsonify({'results': results})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 SafeBalance API Server Starting...")
    print("📊 XGBoost Model: Loaded")
    print("🌐 Server: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
