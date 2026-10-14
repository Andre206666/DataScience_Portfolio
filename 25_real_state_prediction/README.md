# 🏠 House Price Predictor

A machine learning project that predicts house prices through a web application built with Flask.

## 🚀 Live Demo

Try the application: https://datascience-portfolio-1.onrender.com

## 📌 Project Overview

This project uses a Random Forest Regressor to estimate house prices based on property characteristics.

Users can enter property information through a web interface and receive an estimated price. The application also stores prediction history in an SQLite database.

## 🛠️ Technologies

- **Python** — core programming language
- **Pandas** — data manipulation and preprocessing
- **Scikit-learn** — machine learning pipeline and model evaluation
- **Flask** — web application
- **SQLite** — prediction history
- **Render** — deployment

## ⚙️ Machine Learning Workflow

1. Load and inspect the housing dataset.
2. Prepare the data and handle missing feature values through an imputation pipeline.
3. Split the dataset into training and test sets.
4. Train a Random Forest regression model.
5. Evaluate predictions on held-out test data.
6. Save the trained pipeline for use in the web application.

## 📊 Model Performance

Evaluation on the test set:

| Metric | Result |
|---|---:|
| R² | 0.7749 |
| Mean Absolute Error (MAE) | 10,363.18 price units |
| Training samples | 516 |
| Test samples | 129 |

**Interpretation:** The model achieved an R² of approximately 0.775 on the test set. Its predictions had a mean absolute error of 10,363.18 in the dataset's price units.

These results provide a baseline for further experimentation and improvement.

## 💡 Key Features

- House price predictions through a browser-based interface
- A trained machine learning pipeline
- Prediction history stored in SQLite
- A deployed web application

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Andre206666/DataScience_Portfolio.git
cd DataScience_Portfolio/25_real_state_prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

Run the training script that generates `models/house_price_pipeline.joblib`. In this project, use the script that successfully produced that file (currently `data_cleaning.py`, if that remains its actual filename).

### 4. Start the application

```bash
python app.py
```

Open the local URL displayed in the terminal.

## 🔍 Future Improvements

- Compare Random Forest against a simple baseline and other regression models.
- Use cross-validation to estimate performance more robustly.
- Improve feature engineering and hyperparameter tuning.
- Add automated tests for data preprocessing and prediction endpoints.

## 👨‍💻 Author

Data Science student interested in machine learning, Python, and building end-to-end ML applications.

GitHub: https://github.com/Andre206666
