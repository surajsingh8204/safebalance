"""
API Test Script for Predict2Protect
Tests the Flask API endpoints with sample data
"""

import requests
import json
from time import time

# API base URL
BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test the health endpoint"""
    print("\n" + "="*50)
    print("Testing Health Check Endpoint")
    print("="*50)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_single_prediction():
    """Test single company prediction"""
    print("\n" + "="*50)
    print("Testing Single Prediction Endpoint")
    print("="*50)
    
    # Sample company data (from training set)
    sample_data = {
        "X1": 511267,
        "X2": 740998,
        "X3": 833107,
        "X4": 180447,
        "X5": 18373,
        "X6": 70658,
        "X7": 89031,
        "X8": 191226,
        "X9": 336018,
        "X10": 163816,
        "X11": 35163,
        "X12": 201026,
        "X13": 128347,
        "X14": 1024333,
        "X15": 372751,
        "X16": 401483,
        "X17": 1024333,
        "X18": 935302,
        "Division": "D",
        "MajorGroup": "37"
    }
    
    try:
        print("\nSending request...")
        start_time = time()
        response = requests.post(
            f"{BASE_URL}/predict",
            json=sample_data,
            headers={"Content-Type": "application/json"}
        )
        elapsed_time = time() - start_time
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {elapsed_time:.3f} seconds")
        print(f"\nPrediction Results:")
        print(json.dumps(response.json(), indent=2))
        
        result = response.json()
        print(f"\n{'='*50}")
        print(f"🎯 Prediction: {result.get('prediction')}")
        print(f"📊 Risk Score: {result.get('risk_score')}/100")
        print(f"⚠️  Risk Category: {result.get('risk_category')}")
        print(f"{'='*50}")
        
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_batch_prediction():
    """Test batch predictions"""
    print("\n" + "="*50)
    print("Testing Batch Prediction Endpoint")
    print("="*50)
    
    # Sample batch data
    batch_data = {
        "companies": [
            {
                "company_name": "Healthy Corp",
                "X1": 2500000, "X2": 800000, "X3": 1700000,
                "X4": 1200000, "X5": 400000, "X6": 450000,
                "X7": 600000, "X8": 900000, "X9": 3000000,
                "X10": 8000000, "X11": 650000, "X12": 2200000,
                "X13": 1800000, "X14": 800000, "X15": 1300000,
                "X16": 1150000, "X17": 6000000, "X18": 5000000,
                "Division": "D", "MajorGroup": "36"
            },
            {
                "company_name": "Risky Inc",
                "X1": 100000, "X2": 50000, "X3": 50000,
                "X4": 800000, "X5": 200000, "X6": -50000,
                "X7": 30000, "X8": 20000, "X9": 100000,
                "X10": 900000, "X11": -30000, "X12": 50000,
                "X13": 100000, "X14": 700000, "X15": -700000,
                "X16": 180000, "X17": 500000, "X18": 800000,
                "Division": "G", "MajorGroup": "59"
            }
        ]
    }
    
    try:
        print("\nSending batch request...")
        start_time = time()
        response = requests.post(
            f"{BASE_URL}/batch_predict",
            json=batch_data,
            headers={"Content-Type": "application/json"}
        )
        elapsed_time = time() - start_time
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {elapsed_time:.3f} seconds")
        print(f"\nBatch Results:")
        
        results = response.json().get('results', [])
        for i, result in enumerate(results, 1):
            print(f"\n--- Company {i}: {result.get('company_name')} ---")
            print(f"Prediction: {result.get('prediction')}")
            print(f"Risk Score: {result.get('risk_score')}/100")
            print(f"Probability: {result.get('probability')}")
        
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_error_handling():
    """Test error handling with invalid data"""
    print("\n" + "="*50)
    print("Testing Error Handling")
    print("="*50)
    
    # Invalid data (missing required fields)
    invalid_data = {
        "X1": 100000,
        "X2": 50000
        # Missing other required fields
    }
    
    try:
        print("\nSending invalid request...")
        response = requests.post(
            f"{BASE_URL}/predict",
            json=invalid_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        # Error handling should return 400
        return response.status_code == 400
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_all_tests():
    """Run all API tests"""
    print("\n" + "="*60)
    print(" "*15 + "PREDICT2PROTECT API TESTS")
    print("="*60)
    
    tests = [
        ("Health Check", test_health_check),
        ("Single Prediction", test_single_prediction),
        ("Batch Prediction", test_batch_prediction),
        ("Error Handling", test_error_handling)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:.<40} {status}")
    
    print(f"\n{'='*60}")
    print(f"Total: {passed}/{total} tests passed")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    print("="*60)

if __name__ == "__main__":
    print("\n🚀 Starting API Tests...")
    print("⚠️  Make sure the Flask server is running on http://localhost:5000")
    
    input("\nPress Enter to continue...")
    
    run_all_tests()
    
    print("\n✅ Testing complete!")
