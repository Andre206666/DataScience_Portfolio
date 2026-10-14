
from pathlib import Path
import sqlite3
from datetime import datetime

import joblib
import pandas as pd
from flask import Flask, request, render_template_string


PROJECT_DIR = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_DIR / "models" / "house_price_pipeline.joblib"
DATABASE_PATH = PROJECT_DIR / "predictions.db"

FEATURES = ["bedroom", "bathroom", "sqft", "floor"]

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        "Model not found. Run 'python train.py' first."
    )

model = joblib.load(MODEL_PATH)
app = Flask(__name__)


def initialize_database():
    with sqlite3.connect(DATABASE_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                bedroom REAL NOT NULL,
                bathroom REAL NOT NULL,
                sqft REAL NOT NULL,
                floor REAL NOT NULL,
                predicted_price REAL NOT NULL
            )
        """)


initialize_database()


HTML_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>House Price Predictor</title>
</head>
<body>
    <h1>House Price Predictor</h1>

    <form action="/predict" method="POST">
        <label>Bedrooms:
            <input type="number" name="bedroom"
                   min="0" step="1" required>
        </label><br><br>

        <label>Bathrooms:
            <input type="number" name="bathroom"
                   min="0" step="0.5" required>
        </label><br><br>

        <label>Square footage:
            <input type="number" name="sqft"
                   min="1" step="1" required>
        </label><br><br>

        <label>Floor:
            <input type="number" name="floor"
                   min="0" step="1" required>
        </label><br><br>

        <button type="submit">Predict price</button>
    </form>

    {% if prediction_text %}
        <h2>{{ prediction_text }}</h2>
    {% endif %}

    {% if error_text %}
        <p>{{ error_text }}</p>
    {% endif %}

    <p><a href="/history">View prediction history</a></p>
</body>
</html>
"""


HISTORY_PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Prediction History</title>
</head>
<body>
    <h1>Prediction History</h1>

    <table border="1" cellpadding="6">
        <tr>
            <th>Time</th>
            <th>Bedrooms</th>
            <th>Bathrooms</th>
            <th>Sqft</th>
            <th>Floor</th>
            <th>Predicted price</th>
        </tr>
        {% for row in rows %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
            <td>{{ "{:,.2f}".format(row[5]) }}</td>
        </tr>
        {% endfor %}
    </table>

    <p><a href="/">Back to predictor</a></p>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML_PAGE,
        prediction_text="",
        error_text="",
    )


@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = {
            feature: float(request.form[feature])
            for feature in FEATURES
        }

        if not all(
            pd.notna(value) and value != float("inf")
            and value != float("-inf")
            for value in values.values()
        ):
            raise ValueError("Values must be finite numbers.")

        if (
            values["bedroom"] < 0
            or values["bathroom"] < 0
            or values["sqft"] <= 0
            or values["floor"] < 0
        ):
            raise ValueError("Please enter valid positive values.")

        if any(
            values[field] != int(values[field])
            for field in ("bedroom", "sqft", "floor")
        ):
            raise ValueError(
                "Bedrooms, sqft, and floor must be whole numbers."
            )

        input_data = pd.DataFrame(
            [[values[feature] for feature in FEATURES]],
            columns=FEATURES,
        )

        prediction = float(model.predict(input_data)[0])

        with sqlite3.connect(DATABASE_PATH) as conn:
            conn.execute("""
                INSERT INTO predictions (
                    timestamp, bedroom, bathroom,
                    sqft, floor, predicted_price
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                datetime.now().isoformat(timespec="seconds"),
                values["bedroom"],
                values["bathroom"],
                values["sqft"],
                values["floor"],
                prediction,
            ))

        return render_template_string(
            HTML_PAGE,
            prediction_text=f"Predicted price: {prediction:,.2f}",
            error_text="",
        )

    except (ValueError, TypeError, KeyError) as error:
        return render_template_string(
            HTML_PAGE,
            prediction_text="",
            error_text=f"Input error: {error}",
        ), 400


@app.route("/history")
def history():
    with sqlite3.connect(DATABASE_PATH) as conn:
        rows = conn.execute("""
            SELECT timestamp, bedroom, bathroom,
                   sqft, floor, predicted_price
            FROM predictions
            ORDER BY id DESC
        """).fetchall()

    return render_template_string(HISTORY_PAGE, rows=rows)


if __name__ == "__main__":
    app.run(debug=False)
