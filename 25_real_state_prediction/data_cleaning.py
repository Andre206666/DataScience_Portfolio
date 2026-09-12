import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("https://raw.githubusercontent.com/dsrscientist/dataset1/master/house_prices.csv")

print(df.head())
print(df.shape)
print(df.isnull().sum())


numeric_cols = df.select_dtypes(include=["number"]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

thresholds = len(df) * 0.5
df = df.dropna(axis=1, thresh=thresholds)

df = df[df["SalePrice"] <= 20000]

categorical_cols = df.select_dtypes(include=["object", "category"]).columns
for col in categorical_cols:
    df[col] = df[col].astype("category").cat.codes

df["price_per_sfqt"] = df["price"] / df["sfqt_living"]

df["house_age"] = 2024 - df["house_age"]

df["is_renovated"] = (df["yr_renovated"] > 0).astype(int)

X = df.drop(columns=["price", "price_per_sfqt"])
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "linear": LinearRegression(),
    "tree": DecisionTreeRegressor(),
    "random": RandomForestRegressor()
}

scores = {}

for name, model in models.items():
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    score = r2_score(y_test, predictions)
    scores[name] = score

    print(f"{name} R² Score: {score:.4f}")

best_model_name = max(scores, key=scores.get)
print(f"\nBest Model: {best_model_name} (R² = {scores[best_model_name]:.4f})")