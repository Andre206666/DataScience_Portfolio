import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

url = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
df = pd.read_csv(url)

df = df.dropna(subset=['home_score', 'away_score'])

world_cup = df[df['tournament'] == 'FIFA World Cup']

def get_winner(row):
    if row['home_score'] > row['away_score']:
        return row["home_team"]
    elif row['away_score'] > row['home_score']:
        return row["away_team"]
    else:
        return "Draw"
world_cup['winner'] = world_cup.apply(get_winner, axis=1)

wins = world_cup['winner'].value_counts()
home_matches = world_cup['home_team'].value_counts()
away_matches = world_cup['away_team'].value_counts()
total_matches = home_matches.add(away_matches, fill_value=0)

win_rate = (wins / total_matches * 100).sort_values(ascending=False)
print(win_rate)
win_rate.head(10).plot(kind="bar")
plt.title("Win rate")
plt.ylabel("%")
plt.xlabel("Matches")
plt.show()

world_cup["date"] = pd.to_datetime(world_cup["date"])
world_cup["year"] = world_cup["date"].dt.year

goals_by_year = world_cup.groupby('year')[['home_score', 'away_score']].sum()
goals_by_year["total"] = goals_by_year["home_score"] + goals_by_year["away_score"]

goals_by_year["total"].plot(kind="bar")
plt.title("Goals by year")
plt.ylabel("%")
plt.xlabel("Year")
plt.show()

conn = sqlite3.connect("world_cup.db")
c = conn.cursor()
world_cup.to_sql("world_cup", conn, if_exists="replace", index=False)
print("Database Saved!")

query = """
     SELECT country, COUNT(*) as matches_hosted
     FROM world_cup
     GROUP BY country
     ORDER BY matches_hosted DESC
     LIMIT 10
     """
result = pd.read_sql(query, conn)
print(result)


win_rate_dict = win_rate.to_dict()
world_cup["home_win_rate"] = world_cup["home_team"].map(win_rate_dict)
world_cup["away_win_rate"] = world_cup["away_team"].map(win_rate_dict)


world_cup["home_win_rate"] = world_cup["home_win_rate"].fillna(0)
world_cup["away_win_rate"] = world_cup["away_win_rate"].fillna(0)


def simplify_result(row):
    if row['winner'] == row['home_team']:
        return "Home win"
    elif row['winner'] == 'Draw':
        return "Draw"
    else:
        return "Away win"

world_cup["result"] = world_cup.apply(simplify_result, axis=1)
print(world_cup['result'].value_counts())

X = world_cup[["home_win_rate", "away_win_rate", "neutral"]]
y = world_cup["result"]


X_train, X_test, y_train, y_test = train_test_split(X, y)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")




