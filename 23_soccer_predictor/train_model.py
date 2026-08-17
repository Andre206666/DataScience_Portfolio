import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt

profiles = pd.read_csv("all_player_profiles.csv")
stats = pd.read_csv("all_player_stats.csv")

stats = stats.drop(columns=["league"], errors="ignore")
players = pd.merge(profiles, stats, on="player_id")

features = [
    "position",
    "league",
    "minutes_played",
    "goals",
    "assists",
    "expected_goals",
    "expected_assists",
    "rating",
    "total_shots",
    "shots_on_target",
    "tackles",
    "interceptions",
]

df = players[features + ["market_value"]].dropna()

X = pd.get_dummies(df[features], drop_first=True)
y = np.log1p(df["market_value"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = xgb.XGBRegressor(
    n_estimators=300,
    learning_rate=0.03,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
)

model.fit(X_train, y_train)

preds = np.expm1(model.predict(X_test))
y_actual = np.expm1(y_test)

score = r2_score(y_actual, preds)
mae = mean_absolute_error(y_actual, preds)

print(f"Improved R² Score: {score:.2f}")
print(f"Average Prediction Error: €{mae:,.2f}")


importance = pd.Series(model.feature_importances_, index=X.columns)
top_features = importance.nlargest(10)

print("Top 10 Most Important Features:")
print(top_features)

top_features.plot(kind="barh", figsize=(8, 5), color="royalblue")
plt.title("Key Drivers of Footballer Market Value")
plt.xlabel("XGBoost Feature Importance Score")
plt.tight_layout()
plt.show()