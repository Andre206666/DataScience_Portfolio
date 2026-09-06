# Twitter Sentiment Analysis 📝

## Overview
NLP project analyzing 31,962 real tweets using TextBlob and 
Machine Learning to classify sentiment — achieving 95% accuracy
with Logistic Regression and TF-IDF vectorization.

## Key Results
| Metric | Result |
|---|---|
| Dataset size | 31,962 tweets |
| Model accuracy | **95%** |
| Positive tweets | 50% |
| Neutral tweets | 35% |
| Negative tweets | 15% |

## Unexpected Finding 🐻‍❄️
Negative tweets were dominated by environmental concerns —
**"polar bear"** was the most common negative bigram, suggesting
climate anxiety is a significant source of negative sentiment
on social media.

## Machine Learning Pipeline
1. Text preprocessing with NLTK stopword removal
2. TF-IDF vectorization (1000 features)
3. Logistic Regression classifier
4. **95% accuracy** on test set

## Known Limitation
Class imbalance (93% positive training data) causes slight 
bias toward positive predictions — a real-world ML challenge.

## Tech Stack
- **NLP:** NLTK, TextBlob
- **ML:** Scikit-learn (Logistic Regression, TF-IDF)
- **Analysis:** Pandas, Matplotlib
- **Environment:** Jupyter Notebook

## How to run
```bash
pip install nltk textblob scikit-learn pandas
```
Open `sentiment_analysis.ipynb` in Jupyter