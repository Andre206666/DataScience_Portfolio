import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from flask import Flask, request, render_template_string
import sqlite3
from datetime import datetime

print("Downloading data...")

url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/house_price_data.csv"
df = pd.read_csv(url)

df.columns = df.columns.str.lower()

numeric_cols = df.select_dtypes(include=["number"]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

df = df[df["price"] <= 2000000]

X = df[['bedroom', 'bathroom', 'sqft', 'floor']]
y = df['price']

print("Training model...")
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

print("Model trained! Starting Flask server...")

conn = sqlite3.connect('predictions.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        timestamp TEXT,
        bedroom REAL,
        bathroom REAL,
        sqft REAL,
        floor REAL,
        predicted_price REAL
    )
''')
conn.commit()
conn.close()

app = Flask(__name__)

HTML_PAGE = """
<h2>House Price Predictor</h2>
<form action="/predict" method="POST">
    Bedrooms: <input type="number" step="1" name="bedroom" required><br><br>
    Bathrooms: <input type="number" step="0.5" name="bathroom" required><br><br>
    Square Footage: <input type="number" step="1" name="sqft" required><br><br>
    Floor Number: <input type="number" step="1" name="floor" required><br><br>
    <button type="submit">Predict!</button>
</form>
<h3>{{ prediction_text }}</h3>
<br>
<a href="/history">View Prediction History (Database)</a>
"""

HISTORY_PAGE = """
<h2>Database History</h2>
<table border="1" cellpadding="5">
    <tr>
        <th>Time</th>
        <th>Bedrooms</th>
        <th>Bathrooms</th>
        <th>Sqft</th>
        <th>Floor</th>
        <th>Predicted Price</th>
    </tr>
    {% for row in rows %}
    <tr>
        <td>{{ row[0] }}</td>
        <td>{{ row[1] }}</td>
        <td>{{ row[2] }}</td>
        <td>{{ row[3] }}</td>
        <td>{{ row[4] }}</td>
        <td>${{ "{:,.2f}".format(row[5]) }}</td>
    </tr>
    {% endfor %}
</table>
<br>
<a href="/">Go Back to Predictor</a>
"""


@app.route('/')
def home():
    return render_template_string(HTML_PAGE, prediction_text="")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        bedroom = float(request.form['bedroom'])
        bathroom = float(request.form['bathroom'])
        sqft = float(request.form['sqft'])
        floor = float(request.form['floor'])

        input_data = pd.DataFrame([[bedroom, bathroom, sqft, floor]],
                                  columns=['bedroom', 'bathroom', 'sqft', 'floor'])

        prediction = model.predict(input_data)[0]
        output = f"${prediction:,.2f}"

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect('predictions.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO predictions (timestamp, bedroom, bathroom, sqft, floor, predicted_price)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (current_time, bedroom, bathroom, sqft, floor, prediction))
        conn.commit()
        conn.close()

        return render_template_string(HTML_PAGE, prediction_text=f'Predicted Price: {output}')

    except Exception as e:
        return render_template_string(HTML_PAGE, prediction_text='Error: Please enter valid numbers.')


@app.route('/history')
def history():
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM predictions ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()

    from flask import render_template_string
    return render_template_string(HISTORY_PAGE, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)