import pandas as pd

profiles = pd.read_csv('all_player_profiles.csv')
stats = pd.read_csv('all_player_stats.csv')

df = pd.merge(profiles, stats, on='player_id', suffixes=('', '_stats_drop'))

df = df.dropna(subset=['market_value', 'goals', 'minutes_played'])

print(f"TTotal merged players ready for training: {len(df)}")
print(df[['name', 'position', 'goals', 'assists', 'market_value']].head())