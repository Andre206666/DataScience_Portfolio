import pandas as pd

url = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
df = pd.read_csv(url)

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df["tournament"].unique())

df = df.dropna(subset=['home_score', 'away_score'])
print(df.shape)

world_cup = df[df['tournament'] == 'FIFA World Cup']
print(world_cup.shape)
print(world_cup['date'].min())
print(world_cup['date'].max())
print(world_cup.shape)

def get_winner(row):
    if row['home_score'] > row['away_score']:
        return row["home_team"]
    elif row['away_score'] > row['home_score']:
        return row["away_team"]
    else:
        return "Draw"
world_cup['winner'] = world_cup.apply(get_winner, axis=1)
print(world_cup[['home_team', 'away_team', 'winner']].head(10))

wins = world_cup['winner'].value_counts()
home_matches = world_cup['home_team'].value_counts()
away_matches = world_cup['away_team'].value_counts()
total_matches = home_matches.add(away_matches, fill_value=0)
win_rate = (wins / total_matches * 100).sort_values(ascending=False)
print(win_rate.head(10))