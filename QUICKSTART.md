# Quick Start Guide - SafeBalance

## 🚀 Run the Application in 3 Steps

### 1. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Start the Server
```powershell
python app.py
```

### 3. Open Your Browser
Navigate to: **http://localhost:5000**

---

## 📝 Using the Web Interface

1. **Fill in all 18 financial metrics** (X1 through X18)
2. **Select Division** (A, B, C, D, E, F, G, H, or I)
3. **Enter Major Group** code (e.g., 37, 50, 51)
4. **Click "Predict Bankruptcy Risk"**
5. **View Results** - Prediction, Risk Score, and Category

---

## 🧪 Quick Test

Click the **"Load Sample Data"** button to auto-fill with example company data, then click **"Predict Bankruptcy Risk"** to see the model in action!

---

## 📊 Understanding the Results

### Risk Categories
- **Very Low Risk** (0-19%): Healthy financial status
- **Low Risk** (20-34%): Stable, monitor regularly
- **Moderate Risk** (35-49%): Some concerns, investigate
- **High Risk** (50-69%): Significant warning signs
- **Very High Risk** (70-100%): Critical, immediate action needed

### Prediction Outcomes
- **Alive**: Company shows healthy financial indicators
- **Failed**: Company exhibits bankruptcy risk patterns

---

## 🔧 Troubleshooting

**Model not loading?**
- Ensure `xgb_final_model.json` is in the same directory as `app.py`

**Port already in use?**
- Change port in `app.py`: `app.run(port=5001)`

**Missing dependencies?**
- Run: `pip install -r requirements.txt`

---

## 📡 API Usage Example

```python
import requests

data = {
    "X1": 511267, "X2": 740998, "X3": 833107,
    "X4": 180447, "X5": 18373, "X6": 70658,
    "X7": 89031, "X8": 191226, "X9": 336018,
    "X10": 163816, "X11": 35163, "X12": 201026,
    "X13": 128347, "X14": 1024333, "X15": 372751,
    "X16": 401483, "X17": 1024333, "X18": 935302,
    "Division": "D", "MajorGroup": "37"
}

response = requests.post('http://localhost:5000/predict', json=data)
print(response.json())
```

---

**For detailed documentation, see README.md**
