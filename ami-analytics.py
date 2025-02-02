from xml.etree.ElementInclude import include
import functs
import pandas as pd

# Replace 'your_excel_file.xlsx' with the file path to your Excel file.
file_path = '/home/jake-miller/fn-analytics/fn-data/data-export.xlsx'
staff_path = '/home/jake-miller/fn-analytics/fn-data/CS15-Staffs.xlsx'

# Read all sheets into a dictionary of DataFrames
sheets_dict = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')
staff_dict = pd.read_excel(staff_path, sheet_name=None, engine='openpyxl')

# Access each sheet by its name
cs15_df = sheets_dict["CS15"]
ami1_df = sheets_dict["AMI 1"]
ami2_df = sheets_dict["AMI 2"]
pai1_df = sheets_dict["PAI 1"]
sami1_df = sheets_dict["SAMI 1"]
cai1_df = sheets_dict["CAI 1"]
alpha_df = staff_dict["Alpha"]
bravo_df = staff_dict["Bravo"]
charlie_df = staff_dict["Charlie"]
astaff_df = staff_dict["AStaff"]
flight_dfs = {
    "alpha": alpha_df,
    "bravo": bravo_df,
    "charlie": charlie_df,
    "astaff": astaff_df
}

# Calculate for "AMI 1"
functs.calculate_averages_and_failures(cs15_df, flight_dfs, "AMI 1", "AMI 1")

# Calculate for "AMI 2"
functs.calculate_averages_and_failures(cs15_df, flight_dfs, "AMI 2", "AMI 2")

top_three_ami1_infractions = functs.get_top_column_titles_with_most_xs(ami1_df)
print("The top three infractions for AMI 1 are:")
print(top_three_ami1_infractions)

top_three_ami2_infractions = functs.get_top_column_titles_with_most_xs(ami2_df)
print("The top three infractions for AMI 2 are:")
print(top_three_ami2_infractions)