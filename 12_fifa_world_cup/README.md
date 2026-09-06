# FIFA World Cup 2026 Analysis ⚽

## Overview
End-to-end data science analysis of 1,036 real FIFA World Cup 
matches (1930-2026) uncovering historical patterns and predicting 
match outcomes using Machine Learning.

## Live Data Source
Real data from [martj42/international_results](https://github.com/martj42/international_results)
49,493 international matches filtered to World Cup only.

## Key Insights
| Finding | Result |
|---|---|
| Best team historically | Brazil (66.9% win rate) |
| Most matches hosted | USA (118 matches) |
| Home advantage | 483 home wins vs 334 away wins |
| Best month for goals | 2026 projected highest ever |

## Machine Learning
- **Model:** Decision Tree Classifier
- **Features:** home win rate, away win rate, neutral venue
- **Accuracy:** 47% (vs 33% random baseline — 42% improvement)
- **Key finding:** Real data improved accuracy from 35.6% (synthetic) to 47%

## Tech Stack
- **Analysis:** Python, Pandas, NumPy
- **Visualization:** Matplotlib
- **Database:** SQLite
- **ML:** Scikit-learn

## How to run
```bash
python fifa_real_data.py
```

## What makes this project unique
Uses real 96-year historical dataset to validate that genuine 
data patterns significantly outperform synthetic random data 
in ML prediction tasks.