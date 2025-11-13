const form = document.getElementById('predictionForm');
const loading = document.getElementById('loading');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    loading.style.display = 'block';
    result.style.display = 'none';

    const formData = new FormData(form);
    const data = {};
    
    formData.forEach((value, key) => {
        data[key] = isNaN(value) ? value : parseFloat(value);
    });

    try {
        console.log('Sending data:', data);
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const prediction = await response.json();
        console.log('Received prediction:', prediction);
        
        loading.style.display = 'none';
        
        if (prediction.error) {
            alert('Server Error: ' + prediction.error);
        } else {
            displayResult(prediction);
        }
    } catch (error) {
        loading.style.display = 'none';
        console.error('Error:', error);
        alert('Error: ' + error.message);
    }
});

function displayResult(prediction) {
    const isAlive = prediction.prediction === 'Alive';
    const resultClass = isAlive ? 'success' : 'danger';
    const predictionClass = isAlive ? 'alive' : 'failed';

    result.innerHTML = `
        <div class="result-box ${resultClass}">
            <h3 style="margin-bottom: 20px; font-size: 1.5em;">
                ${isAlive ? '✅' : '⚠️'} Prediction Results
            </h3>
            
            <div class="result-item">
                <span class="result-label">Status Prediction:</span>
                <span class="result-value ${predictionClass}">${prediction.prediction}</span>
            </div>
            
            <div class="result-item">
                <span class="result-label">Bankruptcy Probability:</span>
                <span class="result-value">${(prediction.probability * 100).toFixed(2)}%</span>
            </div>
            
            <div class="result-item">
                <span class="result-label">Risk Category:</span>
                <span class="result-value">${prediction.risk_category}</span>
            </div>
            
            <div class="risk-meter">
                <div style="margin-bottom: 10px; font-weight: 600; color: var(--text-secondary);">
                    Risk Score: ${prediction.risk_score}/100
                </div>
                <div class="risk-bar">
                    <div class="risk-fill" style="width: ${prediction.risk_score}%">
                        ${prediction.risk_score}%
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 20px; padding: 15px; background: var(--bg-input); border-radius: 8px;">
                <strong>Interpretation:</strong>
                <p style="margin-top: 10px; color: var(--text-secondary); line-height: 1.6;">
                    ${isAlive 
                        ? 'The company shows healthy financial indicators with low bankruptcy risk. Continue monitoring key metrics regularly.'
                        : 'The company exhibits concerning financial patterns with elevated bankruptcy risk. Immediate attention and corrective measures recommended.'}
                </p>
            </div>
        </div>
    `;
    
    result.style.display = 'block';
}

function resetForm() {
    form.reset();
    result.style.display = 'none';
}

function loadSample() {
    // Sample data from training set
    const sampleData = {
        fyear: 1999,
        X1: 511267,
        X2: 740998,
        X3: 833107,
        X4: 180447,
        X5: 18373,
        X6: 70658,
        X7: 89031,
        X8: 191226,
        X9: 336018,
        X10: 163816,
        X11: 35163,
        X12: 201026,
        X13: 128347,
        X14: 1024333,
        X15: 372751,
        X16: 401483,
        X17: 1024333,
        X18: 935302,
        Division: 'D',
        MajorGroup: '37'
    };

    Object.keys(sampleData).forEach(key => {
        const input = form.elements[key];
        if (input) {
            input.value = sampleData[key];
        }
    });
}
