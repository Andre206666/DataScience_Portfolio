# E-commerce Analytics Platform 🛒

## Live Demo
🌐 https://ecommerce-platform-3zli.onrender.com

## Overview
A production-ready full-stack web application that automatically 
scrapes, analyzes and visualizes e-commerce book data in real-time.
Built to demonstrate end-to-end data engineering and ML skills.

## Features
- 🕷️ **Web Scraping** — automatically collects 100+ books from live website
- 🗄️ **SQL Database** — stores and queries data with SQLite
- 🤖 **Machine Learning** — predicts book ratings using Random Forest
- 📊 **Analytics Dashboard** — 3-page web interface with insights
- 🚀 **Live Deployment** — accessible from anywhere via Render

## Key Insights
- Average book price: £34.56
- Most common rating: Three stars
- No correlation between price and rating quality

## Tech Stack
- **Backend:** Python, Flask, SQLite
- **Data:** BeautifulSoup, Pandas, Scikit-learn
- **Frontend:** HTML, CSS
- **Deployment:** Render (free tier)

## Pages
- `/` — Homepage with real-time stats
- `/products` — Complete book catalog
- `/insights` — Top expensive and highest rated books

## How to run locally
```bash
pip install -r requirements.txt
python app.py
```
Visit http://127.0.0.1:8080