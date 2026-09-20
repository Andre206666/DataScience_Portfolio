# 🏠 House Price Predictor

## Try it live!
👉 https://datascience-portfolio-1.onrender.com

## What is this?
Ever wondered how much a house is worth? This app uses 
Machine Learning to predict house prices based on simple 
inputs like bedrooms, bathrooms and square footage.

Just enter the details and get an instant price estimate!

## How I built it
I started by collecting real housing data, cleaned it up 
(removed outliers, filled missing values), then trained 
a Random Forest model to learn pricing patterns.

I wrapped everything in a Flask web app so anyone can 
use it from their browser — no coding required!

Every prediction gets saved to a database so you can 
track all previous estimates at /history.

## What I learned
- How to take a raw dataset all the way to a live web app
- That Random Forest works really well for price prediction
- Deployment is harder than building the model!

## Tech used
Python • Flask • Scikit-learn • Pandas • SQLite • Render

## Run it yourself
```bash
pip install -r requirements.txt
python app.py
```