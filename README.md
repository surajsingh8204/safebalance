# 🛡️ SafeBalance - Corporate Bankruptcy Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0.3-orange.svg)](https://xgboost.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **PLUTUS'25 Competition Entry** - An advanced machine learning web application for predicting corporate bankruptcy risk using financial intelligence.

![SafeBalance Dashboard](https://via.placeholder.com/1200x400/0f172a/3b82f6?text=SafeBalance+Dashboard)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Data Pipeline](#data-pipeline)
- [Future Enhancements](#future-enhancements)

---

## 🎯 Overview

**SafeBalance** is a sophisticated bankruptcy prediction system that leverages XGBoost machine learning to assess corporate financial health. The system analyzes 18 financial metrics and generates real-time risk assessments with **83.1% accuracy** and **67.3% recall** on failed companies.

### Key Highlights

- ✅ **Trained on 62,782 companies** with real-world financial data
- ✅ **9 engineered financial ratios** for comprehensive analysis
- ✅ **Optimized threshold (0.35)** for balanced precision-recall
- ✅ **Modern web interface** with responsive design
- ✅ **REST API** for batch predictions and integrations

---

## ✨ Features

### 🤖 Machine Learning
- **XGBoost Classifier** with hyperparameter tuning (RandomSearchCV)
- **Feature Engineering**: Current Ratio, Leverage Ratio, Profit Margin, Asset Turnover, Debt-to-Equity, EBIT Margin, Gross Margin, Receivables Ratio, Inventory Turnover
- **Advanced Preprocessing**: Winsorization, log transformation, RobustScaler
- **Class Imbalance Handling**: Scale_pos_weight optimization (14:1 ratio)
- **Threshold Optimization**: Custom threshold (0.35) for better recall

### 🌐 Web Application
- **Interactive Dashboard**: Real-time bankruptcy risk prediction
- **Form Validation**: Smart input validation with tooltips
- **Risk Visualization**: Dynamic risk meter (0-100 scale)
- **Sample Data**: One-click load of example company data
- **Responsive Design**: Mobile-friendly interface

### 🔌 API Endpoints
- `POST /predict` - Single company prediction
- `POST /batch_predict` - Batch predictions for multiple companies
- `GET /health` - API health check

---

## 📊 Model Performance

| Metric | Value | Description |
|--------|-------|-------------|
| **Accuracy** | 83.1% | Overall prediction accuracy |
| **Recall (Failed)** | 67.3% | Correctly identified bankruptcies |
| **Precision (Failed)** | 23.4% | Accuracy of bankruptcy predictions |
| **F1 Score (Failed)** | 34.7% | Harmonic mean of precision & recall |

### Confusion Matrix (Threshold = 0.35)
- **True Positives**: Successfully identified failed companies
- **False Positives**: Alive companies flagged as risky (acceptable for risk management)
- **False Negatives**: Minimized through threshold tuning

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone or Navigate to Project Directory**
   ```powershell
   cd "c:\Users\Suraj\Desktop\coding\mlproject\bankruptcy prediction"
   ```

2. **Create Virtual Environment** (Optional but Recommended)
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Verify Model File**
   Ensure `xgb_final_model.json` exists in the project directory.

---

## 💻 Usage

### Starting the Application

1. **Run the Flask Server**
   ```powershell
   python app.py
   ```

2. **Access the Web Interface**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

### Using the Web Interface

1. **Enter Financial Data**
   - Fill in all 18 financial metrics (X1-X18)
   - Select company Division (A-I)
   - Enter Major Group classification

2. **Submit for Prediction**
   - Click "🔮 Predict Bankruptcy Risk"
   - View real-time results with risk score

3. **Quick Test**
   - Click "📝 Load Sample Data" for pre-filled example
   - Click "🔄 Clear Form" to reset

### Sample Input Data

```json
{
  "X1": 511267,    "X2": 740998,    "X3": 833107,
  "X4": 180447,    "X5": 18373,     "X6": 70658,
  "X7": 89031,     "X8": 191226,    "X9": 336018,
  "X10": 163816,   "X11": 35163,    "X12": 201026,
  "X13": 128347,   "X14": 1024333,  "X15": 372751,
  "X16": 401483,   "X17": 1024333,  "X18": 935302,
  "Division": "D", "MajorGroup": "37"
}
```

---

## 📡 API Documentation

### 1. Single Prediction

**Endpoint**: `POST /predict`

**Request Body**:
```json
{
  "X1": 511267,
  "X2": 740998,
  ...
  "X18": 935302,
  "Division": "D",
  "MajorGroup": "37"
}
```

**Response**:
```json
{
  "prediction": "Alive",
  "probability": 0.1234,
  "risk_score": 12,
  "risk_category": "Low Risk",
  "threshold": 0.35
}
```

### 2. Batch Prediction

**Endpoint**: `POST /batch_predict`

**Request Body**:
```json
{
  "companies": [
    {
      "company_name": "Company A",
      "X1": 511267,
      ...
    },
    {
      "company_name": "Company B",
      "X1": 620000,
      ...
    }
  ]
}
```

**Response**:
```json
{
  "results": [
    {
      "company_name": "Company A",
      "prediction": "Alive",
      "probability": 0.1234,
      "risk_score": 12
    },
    ...
  ]
}
```

### 3. Health Check

**Endpoint**: `GET /health`

**Response**:
```json
{
  "status": "healthy",
  "model": "loaded"
}
```

---

## 📁 Project Structure

```
bankruptcy prediction/
│
├── app.py                      # Flask backend server
├── xgb_final_model.json        # Trained XGBoost model
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/
│   └── index.html              # Web interface
│
├── train.csv                   # Training dataset
├── test.csv                    # Test dataset
├── output.csv                  # Prediction results
│
└── safebalance.ipynb           # Model development notebook
```

---

## 🛠️ Technology Stack

### Backend
- **Flask** - Web framework
- **XGBoost** - Gradient boosting ML algorithm
- **scikit-learn** - Preprocessing & model evaluation
- **pandas** - Data manipulation
- **NumPy** - Numerical computations

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (Custom gradient design)
- **JavaScript** - Interactive functionality
- **Fetch API** - Asynchronous requests

### Model Training
- **Jupyter Notebook** - Experimentation
- **RandomizedSearchCV** - Hyperparameter tuning
- **RobustScaler** - Feature scaling
- **Custom threshold tuning** - Recall optimization

---

## 🔄 Data Pipeline

### 1. Data Cleaning
- Remove unnecessary columns (company_name, Unnamed: 0)
- Drop rare Division 'J' (< 0.01% of data)
- Handle rare MajorGroup values (merge to "Other")

### 2. Encoding
- **Division**: One-hot encoding (8 binary columns)
- **MajorGroup**: Frequency encoding based on occurrence

### 3. Outlier Treatment
- **Winsorization**: Clip values to 1st-99th percentile
- Applied to all 18 financial features (X1-X18)

### 4. Feature Engineering
```python
Current_Ratio = X1 / X14
Leverage_Ratio = X18 / X10
Profit_Margin = X6 / X17
Asset_Turnover = X17 / X10
Debt_to_Equity = X18 / (X10 - X18)
EBIT_Margin = X11 / X17
Gross_Margin = X13 / X17
Receivables_Ratio = X7 / X10
Inventory_Turnover = X2 / X5
```

### 5. Transformation
- **Log transformation**: Applied to all ratio features
- **RobustScaler**: Standardize using median and IQR

### 6. Model Training
- **Algorithm**: XGBoost with scale_pos_weight
- **Tuning**: RandomizedSearchCV (25 iterations, 3-fold CV)
- **Threshold**: Optimized to 0.35 for better recall

---

## 🔮 Future Enhancements

### Short-term
- [ ] **SHAP Analysis**: Add explainability with SHAP values
- [ ] **Feature Importance**: Interactive visualization
- [ ] **CSV Upload**: Batch prediction via file upload
- [ ] **Export Results**: Download predictions as CSV/PDF

### Medium-term
- [ ] **Model Comparison**: LightGBM and CatBoost integration
- [ ] **Ensemble Stacking**: Combine multiple models
- [ ] **Time-series Analysis**: Trend prediction over fiscal years
- [ ] **User Authentication**: Secure login system

### Long-term
- [ ] **Interactive Dashboard**: Real-time metrics with charts
- [ ] **Database Integration**: PostgreSQL for historical data
- [ ] **Docker Deployment**: Containerized application
- [ ] **Cloud Hosting**: AWS/Azure deployment
- [ ] **Mobile App**: iOS and Android applications

---

## 📈 Model Training Summary

### Dataset
- **Training Size**: 62,782 companies
- **Test Size**: 15,893 companies
- **Class Distribution**: 14:1 (Alive:Failed)
- **Features**: 18 financial metrics + 2 categorical

### Hyperparameters (Best from RandomSearchCV)
```python
{
  'subsample': 0.9,
  'scale_pos_weight': 10,
  'reg_lambda': 1.5,
  'n_estimators': 400,
  'max_depth': 7,
  'learning_rate': 0.05,
  'gamma': 0.2,
  'colsample_bytree': 0.8
}
```

### Threshold Analysis
| Threshold | Recall | Precision | F1-Score |
|-----------|--------|-----------|----------|
| 0.30 | 76.0% | 21.3% | 33.2% |
| **0.35** | **67.3%** | **23.4%** | **34.7%** |
| 0.40 | 58.5% | 25.8% | 35.9% |

---

## 👨‍💻 Development Team

**PLUTUS'25 Competition Entry**
- Model Development: XGBoost with advanced feature engineering
- Web Development: Flask + Modern responsive UI
- Data Processing: Comprehensive preprocessing pipeline

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **PLUTUS'25** for organizing the competition
- **XGBoost Community** for the powerful ML framework
- **scikit-learn** for preprocessing tools
- **Flask** for the lightweight web framework

---

## 📞 Support

For issues, questions, or contributions:
1. Check existing documentation
2. Review API endpoints
3. Examine sample data formats
4. Verify model file integrity

---

## 🎓 Educational Value

This project demonstrates:
✅ End-to-end ML pipeline development
✅ Handling severe class imbalance
✅ Advanced feature engineering for financial data
✅ Model deployment with web interface
✅ RESTful API design
✅ Modern frontend development

---

**Built with ❤️ for PLUTUS'25 | SafeBalance © 2025**
