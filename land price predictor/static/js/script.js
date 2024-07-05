document.getElementById('prediction-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    const resultDiv = document.getElementById('prediction-result');

    // Clear previous results
    resultDiv.innerText = '';

    // Validate all required fields
    for (let [key, value] of formData.entries()) {
        if (!value) {
            resultDiv.innerText = `Error: ${key.replace('_', ' ')} is required`;
            return;
        }
    }

    const rate_persqft = parseFloat(formData.get('rate_persqft'));
    const area_insqft = parseFloat(formData.get('area_insqft'));

    if (isNaN(rate_persqft) || isNaN(area_insqft)) {
        resultDiv.innerText = 'Error: Please enter valid numbers for rate and area';
        return;
    }

    try {
        resultDiv.innerText = 'Processing...';

        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(Object.fromEntries(formData)),
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error('Full error response:', errorText);
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }

        const data = await response.json();
        if (data.error) {
            throw new Error(data.error);
        }

        resultDiv.innerText = `Estimated House Price: ₹${data.prediction.toLocaleString('en-IN', { maximumFractionDigits: 2 })} Lakhs`;
    } catch (error) {
        console.error('Error:', error);
        resultDiv.innerText = `Error: ${error.message}`;
    }
});