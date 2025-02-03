import matplotlib.pyplot as plt
import pandas as pd

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


def get_top_column_titles_with_most_xs(df):
    """
    Returns the top three column titles between column indices 10 to 29
    with the most occurrences of "X".

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.Series: Top three column names and their counts as a Series.
    """
    # Select columns 10 through 29 by position
    columns_10_to_29 = df.iloc[:, 10:30]

    # Count the number of "X"s in each column
    column_x_counts = columns_10_to_29.apply(lambda col: (col == "X").sum(), axis=0)

    # Sort columns by count in descending order and pick the top three
    top_columns = column_x_counts.sort_values(ascending=False).head(3)

    return top_columns


def get_ktest_fails(df, ktest_name):
    """
    Finds rows where the score in the `ktest_name` column is less than 80.
    For those rows (people), sums all the scores less than 80 in the columns from 6
    to the column with `ktest_name`, and returns their name and the count of such scores.

    Args:
        df (pd.DataFrame): The input DataFrame, assumed to have a column for names.
        ktest_name (str): The name of the column to check for the threshold (< 80).

    Returns:
        dict: A dictionary where keys are names and values are the sums of scores < 80 in the relevant range.
    """
    # Ensure the ktest_name column exists
    if ktest_name not in df.columns:
        raise ValueError(f"Column '{ktest_name}' not found in the DataFrame.")

    # Dynamically get the index of the ktest_name column
    ktest_col_index = df.columns.get_loc(ktest_name)

    # Filter rows where the score in the ktest_name column is less than 80
    failing_people = df[df[ktest_name] < 80]

    # Initialize the result dictionary
    result = {}

    # Loop through each person who failed the ktest
    for _, row in failing_people.iterrows():
        # Get their name (assuming the name column is the first column, i.e., index 0)
        person_name = row["Last Name"]

        # Select columns from 5 through ktest_name (inclusive)
        relevant_scores = row.iloc[5: ktest_col_index + 1]

        # Count the number of scores less than 80 for this person
        num_scores_below_80 = (relevant_scores < 80).sum()

        # Add to the result dictionary
        result[person_name] = num_scores_below_80

    return result

def get_ktest_averages(ktest_df, flight_dfs, ktest_name):
    # Calculate flight averages
    squad_average = ktest_df[ktest_name].mean()
    print("The average score for the squad is: ", squad_average)
    for flight_name, flight_df in flight_dfs.items():
        flight_subset = ktest_df[ktest_df['Last Name'].isin(flight_df["Name"].apply(lambda x: x.split()[-1]))]
        flight_average = flight_subset[ktest_name].mean()
        print(f"{flight_name.title()} K-Test Average: {flight_average:.2f}")
