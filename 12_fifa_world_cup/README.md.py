# FIFA World Cup 2026 Analysis ⚽

## Description
An end-to-end data analysis project exploring international
football match data — covering team performance, confederation
strength, goal trends, and a machine learning model to predict
match outcomes.

## Tech Stack
- Python Pandas, NumPy
- Matplotlib
- SQLite
- Scikit-learn Machine Learning

## Key Insights
- **USA has the best win rate 46.2%** despite Germany having
  more total wins — win rate is a stronger indicator of
  consistency than total wins.
- **UEFA dominates** with 174 wins, more than double CONCACAF
  and CONMEBOL — reflecting the high competitive level of
  European leagues.
- **Goal trends remained stable** across complete seasons, with
  apparent declines explained by incomplete data at dataset edges.

## Machine Learning
A Decision Tree model was trained to predict match outcomes
Home Win / Away Win / Draw using team win rates as features.
The model achieved 35.6% accuracy — only marginally above random
guessing 33%, demonstrating that synthetic random data lacks
the real signal needed for meaningful prediction. This highlights
the importance of using authentic historical data for production
models.

## Limitations
This project uses synthetic data due to data sourcing constraints.
Future work should incorporate real historical match data e.g.
from Kaggle's International Football Results dataset) to validate
findings against real-world patterns.

## How to run
python fifa_analysis.py