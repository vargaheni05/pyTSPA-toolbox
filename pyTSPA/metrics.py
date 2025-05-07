import numpy as np
import pandas as pd
def result_stats(df):
    """
    Computes the number of home wins, draws, and away wins from full-time result column (FTR).
    Assumes:
        'H' = home win, 'D' = draw, 'A' = away win
    """
    if 'FTR' not in df.columns:
        raise ValueError("Column 'FTR' (full-time result) not found.")

    result_counts = df['FTR'].value_counts().to_dict()
    return {
        'Home Wins': result_counts.get('H', 0),
        'Draws': result_counts.get('D', 0),
        'Away Wins': result_counts.get('A', 0)
    }

def team_performance(df, team_name):
    """
    Summarizes a team's performance across the season.
    Returns stats like matches played, wins, draws, losses, goals scored/conceded.
    """
    matches = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)]

    wins = draws = losses = goals_for = goals_against = 0

    for _, row in matches.iterrows():
        if row['HomeTeam'] == team_name:
            gf, ga = row['FTHG'], row['FTAG']
            result = row['FTR']
            if result == 'H': wins += 1
            elif result == 'D': draws += 1
            else: losses += 1
        else:  # Away team
            gf, ga = row['FTAG'], row['FTHG']
            result = row['FTR']
            if result == 'A': wins += 1
            elif result == 'D': draws += 1
            else: losses += 1

        goals_for += gf
        goals_against += ga

    return {
        'Team': team_name,
        'Matches': len(matches),
        'Wins': wins,
        'Draws': draws,
        'Losses': losses,
        'Goals For': goals_for,
        'Goals Against': goals_against,
        'Goal Difference': goals_for - goals_against,
        'Points': 3 * wins + draws
    }


def get_all_teams(df):
    """
    Returns a list of all unique team names from 'HomeTeam' and 'AwayTeam' columns.
    """
    home_teams = df['HomeTeam'].astype(str).unique()
    away_teams = df['AwayTeam'].astype(str).unique()
    all_teams = np.union1d(home_teams, away_teams)
    return all_teams

def each_team_performance(df):
    """
    Summarizes performance for every team in the dataset using summarize_team_performance().
    Returns a DataFrame where each row is a team's statistics.
    """
    teams = get_all_teams(df)
    summaries = [team_performance(df, team) for team in teams]
    return pd.DataFrame(summaries).sort_values(by='Points', ascending=False).reset_index(drop=True)




#from this point the plotting is implementeed
import seaborn as sns
import matplotlib.pyplot as plt

def plot_result_distribution(df):
    """
    Visualizes overall result distribution: Home Wins, Draws, Away Wins.
    """
    results = result_stats(df)
    result_names = list(results.keys())
    result_counts = list(results.values())

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.barplot(x=result_names, y=result_counts, palette="muted")
    plt.title("Match Result Distribution")
    plt.ylabel("Number of Matches")
    plt.xlabel("Result")
    plt.tight_layout()
    plt.show()


def plot_team_results(df, team_name):
    """
    Plots wins, draws, and losses for a single team.
    """
    stats = team_performance(df, team_name)
    results = {
        'Wins': stats['Wins'],
        'Draws': stats['Draws'],
        'Losses': stats['Losses']
    }

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.barplot(x=list(results.keys()), y=list(results.values()), palette="deep")
    plt.title(f"{team_name} - Match Outcomes")
    plt.ylabel("Number of Matches")
    plt.xlabel("Result Type")
    plt.tight_layout()
    plt.show()

def plot_league_points_table(df):
    """
    Plots total points for all teams as a horizontal bar chart.
    Assumes df is the output of `each_team_performance()`.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 12))
    sorted_df = df.sort_values(by="Points", ascending=True)

    sns.barplot(x="Points", y="Team", data=sorted_df, palette="viridis")
    plt.title("League Table - Points by Team")
    plt.xlabel("Points")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.show()


