import pandas as pd

profiles_df = pd.read_csv('all_player_profiles.csv')
stats_df = pd.read_csv('all_player_stats.csv')

print("--- PROFILES COLUMNS -_--")
print(profiles_df.columns.tolist())

print("\n--- STATS COLUMNS ---")
print(stats_df.columns.tolist())