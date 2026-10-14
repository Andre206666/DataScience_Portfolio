# ⚽ Football Player Market Value Predictor

An end-to-end machine learning project that estimates football players' market values from player positions, leagues, and performance statistics.

## Project Overview

This project explores whether on-field performance metrics can help estimate a football player's market value.

The model uses XGBoost regression and a log-transformed target to handle the highly skewed distribution of player valuations.

## Features

- Merges player profile and performance datasets.
- Analyzes missing values and market value distributions.
- Encodes categorical variables such as league and position.
- Imputes missing numerical and categorical feature values within a machine learning pipeline.
- Compares XGBoost against a median-prediction baseline.
- Evaluates predictions using R², MAE, and RMSE.
- Visualizes the most important model features.
- Saves the trained pipeline for future predictions.

## Dataset

The project uses two CSV files:

- `all_player_profiles.csv`
- `all_player_stats.csv`

The files are joined using `player_id`. Players without a known positive market value are excluded from supervised model training.

The model currently uses the following features:

**Categorical:** position, league.

**Numerical:** minutes played, goals, assists, expected goals, expected assists, rating, total shots, shots on target, tackles, and interceptions.

## Tech Stack

- Python
- Pandas
- NumPy
- scikit-learn
- XGBoost
- Matplotlib
- Joblib

## Evaluation

The model is evaluated on a held-out test set.

Metrics:

- **R²:** coefficient of determination.
- **MAE:** mean absolute prediction error in the dataset's price units.
- **RMSE:** root mean squared error, which penalizes large errors more heavily.

A median baseline is included to check whether XGBoost improves over a simple prediction strategy.

Results should be updated after running the current training script.

## Run Locally

Install dependencies:

```bash
pip install pandas numpy scikit-learn xgboost matplotlib joblib
```

Explore the data:

```bash
python explore_data.py
```

Train and evaluate the model:

```bash
python train_model.py
```

The trained model artifact is saved to:

`models/xgboost_market_value.joblib`

## Limitations

- Market values can depend on age, contract length, injuries, reputation, and other factors not included in the current feature set.
- Missing performance statistics may not be random across leagues or players.
- A random train/test split evaluates predictions for held-out rows from the available dataset, not necessarily future seasons.
- Feature importance indicates how the trained model uses features; it does not establish causation.

## Author

Data Science student interested in machine learning, Python, and end-to-end ML systems.

GitHub: https://github.com/Andre206666
