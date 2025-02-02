import matplotlib.pyplot as plt


# Plot the selected columns as a table and save as an image
def output_table_as_image(df, title, file_name="output.png"):
    # Set up the plot
    fig, ax = plt.subplots(figsize=(6, 2))  # Adjust width and height

    # Remove axes
    ax.axis("tight")
    ax.axis("off")

    # Create table from DataFrame
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center")

    # Add title
    plt.title(title, fontsize=14, pad=10)

    # Save the table as an image
    plt.savefig(file_name, dpi=300, bbox_inches="tight")
    plt.close()

def calculate_averages_and_failures(cs15_df, flight_dfs, column_name, title_prefix):
    """
    Calculates and reports squadron and flight-level averages and outputs tables for failing rooms.

    Args:
        cs15_df (pd.DataFrame): Main dataframe containing the data.
        flight_dfs (dict): Dictionary of flight dataframes with keys as flight names (e.g., "alpha", "bravo", "charlie").
        column_name (str): The column (e.g., "AMI 1", "AMI 2", etc.) to calculate averages and failures for.
        title_prefix (str): Prefix for the table and print statements (e.g., "AMI 1", "AMI 2").
    """
    # Find all fails for the given column
    failing_rooms = cs15_df[cs15_df[column_name] < 80]
    fails_df = failing_rooms[["Name", column_name]]
    output_table_as_image(
        fails_df, title=f"{title_prefix} Failures", file_name=f"outputs/{title_prefix.replace(' ', '_')}_fails.png"
    )

    # Calculate squadron average for the given column
    squadron_average = cs15_df[column_name].mean()
    print(f"{title_prefix} Average: {squadron_average:.2f}")

    # Calculate flight averages
    for flight_name, flight_df in flight_dfs.items():
        flight_subset = cs15_df[cs15_df['Name'].isin(flight_df["Name"])]
        flight_average = flight_subset[column_name].mean()
        print(f"{title_prefix} {flight_name.title()} Average: {flight_average:.2f}")