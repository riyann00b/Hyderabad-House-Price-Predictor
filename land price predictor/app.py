from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.exceptions import NotFittedError

app = Flask(__name__)

# Load the model
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: model.pkl file not found. Please ensure the model file is in the correct location.")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please check server logs.'}), 500

    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data received'}), 400
        
        # Create a DataFrame with the input data
        input_data = pd.DataFrame({
            'title': [data.get('title', '')],
            'location': [data.get('location', '')],
            'rate_persqft': [float(data.get('rate_persqft', 0))],
            'area_insqft': [float(data.get('area_insqft', 0))],
            'building_status': [data.get('building_status', '')]
        })
        
        # Validate input data
        if input_data['rate_persqft'].iloc[0] <= 0 or input_data['area_insqft'].iloc[0] <= 0:
            return jsonify({'error': 'Rate per sqft and Area in sqft must be positive numbers'}), 400
        
        # Make prediction
        prediction = model.predict(input_data)
        output = round(prediction[0], 2)
        
        return jsonify({'prediction': output})
    
    except NotFittedError:
        return jsonify({'error': 'Model is not fitted yet. Please train the model before making predictions.'}), 500
    except ValueError as ve:
        return jsonify({'error': f'Invalid input data: {str(ve)}'}), 400
    except Exception as e:
        app.logger.error(f'An unexpected error occurred: {str(e)}')
        return jsonify({'error': 'An unexpected error occurred. Please check server logs for details.'}), 500

if __name__ == "__main__":
    app.run(debug=True)