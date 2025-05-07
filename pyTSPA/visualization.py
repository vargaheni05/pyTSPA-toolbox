import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plotting(wdl_stats, team_summary):
    """
    Plots:
    1. A Seaborn pie chart of league-wide Win/Draw/Loss stats
    2. A Seaborn bar chart of a team's Wins, Draws, Losses, and Goals
    """
    # Apply Seaborn theme
    sns.set_theme(style="whitegrid")

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # --- Pie Chart using Seaborn-compatible approach ---
    wdl_df = pd.DataFrame(list(wdl_stats.items()), columns=['Result', 'Count'])
    axs[0].pie(
        wdl_df['Count'],
        labels=wdl_df['Result'],
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("pastel")
    )
    axs[0].set_title('League Results Distribution', fontsize=14)

    # --- Bar Chart using Seaborn ---
    performance_data = {
        'Metric': ['Wins', 'Draws', 'Losses', 'Goals For', 'Goals Against'],
        'Value': [
            team_summary['Wins'],
            team_summary['Draws'],
            team_summary['Losses'],
            team_summary['Goals For'],
            team_summary['Goals Against']
        ]
    }
    perf_df = pd.DataFrame(performance_data)

    sns.barplot(data=perf_df, x='Metric', y='Value', ax=axs[1], palette="deep")
    axs[1].set_title(f"{team_summary['Team']} Season Summary", fontsize=14)
    axs[1].bar_label(axs[1].containers[0], label_type='edge')

    plt.tight_layout()
    plt.show()
