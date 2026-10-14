from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent

PROFILES_PATH = BASE_DIR / "all_player_profiles.csv"
STATS_PATH = BASE_DIR / "all_player_stats.csv"


def load_data():
    print("Loading player data...")

    profiles = pd.read_csv(PROFILES_PATH)
    stats = pd.read_csv(STATS_PATH)

    print(f"Profiles shape: {profiles.shape}")
    print(f"Stats shape: {stats.shape}")

    return profiles, stats

def merge_data(profiles, stats):
    required_profile_columns = {
        "player_id", "name", "league", "position", "market_value"
    }

    required_stats_columns = {
        "player_id", "league", "minutes_played", "goals", "assists",
        "expected_goals", "expected_assists", "rating", "total_shots",
        "shots_on_target", "tackles", "interceptions"
    }

    missing_profiles = required_profile_columns - set(profiles.columns)
    missing_stats = required_stats_columns - set(stats.columns)

    if missing_profiles:
        raise ValueError(
            f"Missing profile columns: {sorted(missing_profiles)}"
        )

    if missing_stats:
        raise ValueError(
            f"Missing statistics columns: {sorted(missing_stats)}"
        )

    print("\nDuplicate player IDs")
    print("Profiles:", profiles["player_id"].duplicated().sum())
    print("Stats:", stats["player_id"].duplicated().sum())

    if profiles["player_id"].duplicated().any():
        raise ValueError("Profiles contains duplicate player IDs.")

    if stats["player_id"].duplicated().any():
        raise ValueError("Stats contains duplicate player IDs.")

    players = pd.merge(
        profiles,
        stats,
        on="player_id",
        how="inner",
        suffixes=("_profile", "_stats"),
        validate="one_to_one"
    )

    print("\nMerged shape:", players.shape)

    league_mismatch = (
        players["league_profile"].fillna("MISSING")
        != players["league_stats"].fillna("MISSING")
    )

    print("League mismatches:", int(league_mismatch.sum()))

    return players

def prepare_data(players):
    players = players.drop(columns=["league_stats"]).copy()
    players = players.dropna(subset=["market_value"]).copy()

    players = players[
        players["market_value"] > 0
    ].copy()

    return players

def analyze_missing_values(players):
    features = [
        "position",
        "league_profile",
        "minutes_played",
        "goals",
        "assists",
        "expected_goals",
        "expected_assists",
        "rating",
        "total_shots",
        "shots_on_target",
        "tackles",
        "interceptions",
    ]

    print("\nMissing values in selected features:")
    print(players[features].isna().sum())

    for column in ["expected_goals", "expected_assists"]:
        missing = players[column].isna()

        print(f"\nMissing-value analysis: {column}")
        print(f"Missing rows: {int(missing.sum())}")
        print(f"Missing percentage: {missing.mean() * 100:.2f}%")

        if missing.any():
            by_league = (
                players.groupby("league_profile")[column]
                .agg(
                    total_players="size",
                    missing_count=lambda s: s.isna().sum()
                )
            )

            by_league["missing_pct"] = (
                by_league["missing_count"]
                / by_league["total_players"]
                * 100
            ).round(2)

            print("\nBy league:")
            print(
                by_league.sort_values(
                    "missing_pct", ascending=False
                ).head(15)
            )

            by_position = (
                players.groupby("position")[column]
                .agg(
                    total_players="size",
                    missing_count=lambda s: s.isna().sum()
                )
            )

            by_position["missing_pct"] = (
                by_position["missing_count"]
                / by_position["total_players"]
                * 100
            ).round(2)

            print("\nBy position:")
            print(by_position.sort_values("missing_pct", ascending=False))


def analyze_market_value(players):
    target = players["market_value"]

    print("\nMarket value summary:")
    print(target.describe())

    print("\nMarket value quantiles:")
    print(target.quantile([0.25, 0.50, 0.75, 0.90, 0.95, 0.99]))

    print("\nPlayers by position:")
    print(players["position"].value_counts())

    print("\nPlayers by league:")
    print(players["league_profile"].value_counts())

    plt.figure(figsize=(9, 5))
    plt.hist(target / 1_000_000, bins=40)
    plt.title("Distribution of Football Player Market Values")
    plt.xlabel("Market value (millions of dataset currency units)")
    plt.ylabel("Number of players")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(9, 5))
    plt.hist(
        __import__("numpy").log1p(target),
        bins=40
    )
    plt.title("Log-Transformed Market Value Distribution")
    plt.xlabel("log1p(market value)")
    plt.ylabel("Number of players")
    plt.tight_layout()
    plt.show()

def main():
    profiles, stats = load_data()
    players = merge_data(profiles, stats)
    players = prepare_data(players)

    print("\nClean dataset shape:", players.shape)
    print("Unique player IDs:", players["player_id"].nunique())
    print(
        "Missing market values:",
        players["market_value"].isna().sum()
    )

    analyze_missing_values(players)
    analyze_market_value(players)


if __name__ == "__main__":
    main()
