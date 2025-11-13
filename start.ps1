# Predict2Protect Startup Script
# This script sets up and runs the Predict2Protect web application

Write-Host "=================================" -ForegroundColor Cyan
Write-Host "   Predict2Protect - Startup    " -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check if model file exists
Write-Host "Checking model file..." -ForegroundColor Yellow
if (Test-Path "xgb_final_model.json") {
    Write-Host "✓ Model file found" -ForegroundColor Green
} else {
    Write-Host "✗ Model file (xgb_final_model.json) not found!" -ForegroundColor Red
    exit 1
}

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

# Start the Flask application
Write-Host ""
Write-Host "=================================" -ForegroundColor Cyan
Write-Host "   Starting Flask Server...     " -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🌐 Access the application at: http://localhost:5000" -ForegroundColor Green
Write-Host "📊 API endpoints available at: http://localhost:5000/predict" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Run the application
python app.py
