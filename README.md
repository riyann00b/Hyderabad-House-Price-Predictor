# Hyderabad House Price Predictor

## Overview

The Hyderabad House Price Predictor is a machine learning project that aims to predict house prices in Hyderabad based on various features like location, rate per square foot, area in square feet, building status, and title. This project utilizes a RandomForestRegressor model with an elaborate preprocessing pipeline to ensure accurate predictions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/HyderabadHousePricePredictor.git
    ```
2. Navigate to the project directory:
    ```bash
    cd HyderabadHousePricePredictor
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Model Training and Evaluation

1. Ensure you have the dataset `Hyderabad_House_price.csv` in the project directory.
2. Run the model training script:
    ```bash
    python app.py
    ```
3. The script will output model evaluation metrics such as Mean Absolute Error, Root Mean Squared Error, R-squared score, and Cross-validation RMSE scores. It will also save the trained model as `house_price_model.pkl` and `model.pkl`.

### Predicting House Prices

1. To use the trained model for predictions, ensure the Flask app is running.
2. Input the required details like title, location, rate per sqft, area in sqft, and building status into the form provided in the Flask app.
3. The app will return the predicted house price based on the input features.

## Features

- Predict house prices based on various features.
- Remove duplicates and handle missing values in the dataset.
- Preprocess numerical, categorical, and location features.
- Evaluate the model using various metrics and cross-validation.
- Visualize feature importance.

## Dependencies

- pandas
- numpy
- scikit-learn
- joblib
- pickle
- category_encoders
- matplotlib
- seaborn
- Flask

Install the dependencies using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
