# ⚽ European Football Player Valuation Predictor XGBoost

An end-to-end Machine Learning pipeline that predicts European soccer players' transfer market values based on their in-game performance metrics, league, and position.

## 📊 Results & Performancee

* **Model:** XGBoost Regressor (`n_estimators=300`, `learning_rate=0.03`, `max_depth=6`)
* **R² Score:** 0.444
* **Mean Absolute Error (MAE):** €6,758,322.65
* **Target Transformation:** $\log(1 + y)$ transformation applied to normalize highly skewed superstar valuations.

## 🛠️ Tech Stackg

* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-learn, XGBoost
* **Visualization:** Matplotlib

## 🔍 Features Used

* **Performance Metrics:** Goals, Assists, Expected Goals (xG), Expected Assists (xA), Shots on Target, Total Shots, Tackles, Interceptions, Rating, Minutes Played.
* **Categorical Drivers:** Player Position, League (One-Hot Encoded).

## 🚀 How to Run

1. Clone the repository and install dependencies:
```bash
pip install pandas numpy scikit-learn xgboost matplotlib