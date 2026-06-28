import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


teams = ['Brazil', 'Argentina', 'France', 'Germany', 'Spain', 'England', 'Mexico', 'USA']

df = pd.DataFrame({
    'date': pd.date_range('2020-01-01', periods=500, freq='W'),
    'home_team': np.random.choice(teams, 500),
    'away_team': np.random.choice(teams, 500),
    'home_score': np.random.randint(0, 5, 500),
    'away_score': np.random.randint(0, 5, 500),
    'tournament': np.random.choice(['World Cup', 'Friendly', 'Qualifier'], 500)
})

print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.info())

weird_rows = df[df['home_team'] == df['away_team']]
print(weird_rows)

df = df[df["home_team"] != df["away_team"]]
print(df.shape)

home_goals = df.groupby("home_team")["home_score"].sum()
away_goals = df.groupby("away_team")["away_score"].sum()

total_goals = home_goals.add(away_goals, fill_value=0)
print(total_goals.sort_values(ascending=False))

def get_winner(row):
    if row['home_score'] > row['away_score']:
        return row['home_team']
    elif row['away_score'] > row['home_score']:
        return row['away_team']
    else:
        return 'Draw'

df['winner'] = df.apply(get_winner, axis=1)
print(df[['home_team', 'away_team', 'home_score', 'away_score', 'winner']].head(10))

wins = df["winner"].value_counts()
print(wins)

home_matches = df["home_team"].value_counts()
away_macthes = df["away_team"].value_counts()

total_matches = home_matches.add(away_macthes, fill_value=0)
print(total_matches)

win_rate = (wins / total_matches * 100).sort_values(ascending=False)
print(win_rate)

avg_home_goals = df["home_score"].mean()
avg_away_goals = df["away_score"].mean()

print(f"Average home goals: {avg_home_goals}")
print(f"Average away goals: {avg_away_goals}")

df['year'] = df['date'].dt.year
goals_by_year = df.groupby('year')[['home_score', 'away_score']].sum()
print(goals_by_year)

goals_by_year["total"] = goals_by_year["home_score"] + goals_by_year["away_score"]
goals_by_year["total"].plot(kind="line")
plt.title("Goals by year")
plt.ylabel("Goals")
plt.xlabel("Year")
plt.show()

confederations = {
    "Brazil": "CONMEBOL",
    "Argentina": "CONMEBOL",
    "France": "UEFA",
    "Germany": "UEFA",
    "Spain": "UEFA",
    "England": "UEFA",
    "Mexico": "CONCACAF",
    "USA": "CONCACAF"
}

df['home_confederation'] = df['home_team'].map(confederations)
print(df[["home_team", "home_confederation"]].head(10))

df["away_confederation"] = df["away_team"].map(confederations)
print(df[["away_team", "away_confederation"]].head(10))

df["winner_confederation"] = df["winner"].map(confederations)
print(df[["winner", "winner_confederation"]].head(10))

confederations_wins = df["winner_confederation"].value_counts()
print(confederations_wins)

confederations_wins.plot(kind="bar")
plt.title("Confederations wins")
plt.ylabel("Confederations")
plt.xlabel("Confederations")
plt.show()

plt.scatter(df["home_score"], df["away_score"])
plt.title("home_score vs away_score")
plt.ylabel("Score")
plt.xlabel("Score")
plt.show()


df['home_score'].value_counts().sort_index().plot(kind='bar')
plt.title('Distribution of Home Goals')
plt.xlabel('Goals Scored')
plt.ylabel('Frequency')
plt.show()

conn = sqlite3.connect("fifa.db")
df.to_sql("matches", conn, if_exists="replace")
print("Database created!")

result = pd.read_sql_query("SELECT * FROM matches", conn)
print(result)

query = """
      SELECT winner_confederation, COUNT(*) as wins
      FROM matches
      GROUP BY winner_confederation
      ORDER BY wins DESC
      """

result = pd.read_sql_query(query, conn)
print(result)

query2 = """
       SELECT home_team, SUM(home_score) as total_home_goals
       FROM matches
       GROUP BY home_team
       ORDER BY total_home_goals DESC
       LIMIT 5
       """
result = pd.read_sql_query(query2, conn)
print(result)

win_rate_dict = win_rate.to_dict()
print(win_rate_dict)

df["home_win_rate"] = df["home_team"].map(win_rate_dict)
df["away_win_rate"] = df["away_team"].map(win_rate_dict)

print(df[["home_team", "home_win_rate", "away_team", "away_win_rate"]].head(10))

def simplify_results(row):
    if row["winner"] == row["home_team"]:
        return "Home win"
    elif row["winner"] == "Draw":
        return "Draw"
    else:
        return "Away win"

df["result"] = df.apply(simplify_results, axis=1)
print(df["result"].value_counts())

X = df[["home_win_rate", "away_win_rate"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2%}")
