# Titanic Survival Analysis 🚢

## Overview
Exploratory data analysis and machine learning project predicting 
Titanic passenger survival using real historical data from 1912.
Built in Jupyter Notebook demonstrating the full data science pipeline.

## Key Findings
| Finding | Result |
|---|---|
| Female survival rate | 74% |
| Male survival rate | 19% |
| 1st class survival | 63% |
| 3rd class survival | 24% |
| Strongest predictor | Passenger class (-0.34 correlation) |

## Machine Learning
- **Model:** Decision Tree Classifier
- **Accuracy:** 75.42%
- **Features:** Pclass, Age, Fare, SibSp, Parch, Sex
- **Train/Test split:** 80/20

## Data Cleaning
- Filled missing Age values with median
- Dropped Cabin column (77% missing)
- Filled 2 missing Embarked values with mode

## Tech Stack
- **Analysis:** Python, Pandas
- **Visualization:** Matplotlib
- **ML:** Scikit-learn
- **Environment:** Jupyter Notebook

## Key Insight
Wealth and gender were the primary survival factors —
first class women survived at nearly 10x the rate of 
third class men.

## How to run
```bash
pip install pandas matplotlib scikit-learn
```
Open `titanic_analysis.ipynb` in Jupyter