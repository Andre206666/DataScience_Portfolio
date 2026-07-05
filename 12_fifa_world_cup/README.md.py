# FIFA World Cup Analysis ⚽

## Description
Analysis of REAL historical FIFA World Cup data (1930-2026)
sourced from martj42/international_results, examining team
win rates and historical performance.

## Tech Stack
- Python (Pandas, NumPy)

## Key Insights
- Brazil has the highest win rate in World Cup history (66.7%)
- Top 5 teams by win rate: Brazil, Germany, France,
  Netherlands, Argentina — matches real football consensus
- Dataset includes 1,036 real World Cup matches from 1930-2026

## Data Source
https://github.com/martj42/international_results

## How to run
python fifa_real_data.py

## Additional Key Insights
- USA has hosted the most World Cup matches (116),
  confirming their importance as a host nation for 2026
- 2026 World Cup projected to have most goals ever
  due to expanded 48-team format

## Machine Learning Results
- Synthetic data model: 35.6% accuracy (barely above random 33%)
- Real data model: 47% accuracy — significant improvement
- Features used: home win rate, away win rate, neutral venue
- This validates that real historical patterns improve predictions

# FIFA World Cup 2026 Analysis ⚽

## Description
End-to-end data science project analyzing real FIFA World Cup
data (1,036 matches, 1930-2026) to uncover historical patterns
and predict match outcomes.

## Data Source
Real data from martj42/international_results (49,493 matches)
Filtered to FIFA World Cup matches only.

## Tech Stack
- Python (Pandas, NumPy)
- Matplotlib
- SQLite
- Scikit-learn

## Key Insights
- Brazil has the highest World Cup win rate (66.9%)
- USA has hosted the most World Cup matches (118)
- Home teams win significantly more (483 vs 334 away wins)
- 2026 projected to have most goals ever (48-team format)

## Machine Learning
- Features: home win rate, away win rate, neutral venue
- Model: Decision Tree Classifier
- Accuracy: 43% (vs 33% random baseline)

## How to run
python fifa_real_data.py