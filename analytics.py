from xml.etree.ElementInclude import include
import functs
import pandas as pd

# Replace 'your_excel_file.xlsx' with the file path to your Excel file.
file_path = '/home/jake-miller/fn-analytics/fn-data/data-export.xlsx'
staff_path = '/home/jake-miller/fn-analytics/fn-data/CS15-Staffs.xlsx'
ktest_path = '/home/jake-miller/fn-analytics/fn-data/ktests.xlsx'
othersq_ami2_path = '/home/jake-miller/fn-analytics/fn-data/CS16-Data.xlsx'
othersq_ami1_path = '/home/jake-miller/fn-analytics/fn-data/CS17-Data.xlsx'
# Read all sheets into a dictionary of DataFrames
othersq_ami1_dict = pd.read_excel(othersq_ami1_path, sheet_name=None, engine='openpyxl')
othersq_ami2_dict = pd.read_excel(othersq_ami2_path, sheet_name=None, engine='openpyxl')
sheets_dict = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')
staff_dict = pd.read_excel(staff_path, sheet_name=None, engine='openpyxl')
ktests_dict = pd.read_excel(ktest_path, sheet_name=None, engine='openpyxl')

# Access each sheet by its name
othersq_ami_1 = othersq_ami1_dict["AMI 1"]
othersq_ami_2 = othersq_ami2_dict["AMI 2"]
ktest_df = ktests_dict["Scores"]
cs15_df = sheets_dict["CS15"]
ami1_df = sheets_dict["AMI 1"]
ami2_df = sheets_dict["AMI 2"]
ami3_df = sheets_dict["AMI 3"]
pai1_df = sheets_dict["PAI 1"]
pai2_df = sheets_dict["PAI 2"]
sami1_df = sheets_dict["SAMI 1"]
sami2_df = sheets_dict["SAMI 2"]
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
#functs.calculate_averages_and_failures(cs15_df, flight_dfs, "AMI 1", "AMI 1")

# Calculate for "AMI 2"
#functs.calculate_averages_and_failures(cs15_df, flight_dfs, "AMI 2", "AMI 2")

# Calculate for "AMI 3"
functs.calculate_averages_and_failures(cs15_df, flight_dfs, "AMI 3", "AMI 3")

# Calculate for "SAMI 2"
functs.calculate_averages_and_failures(cs15_df, flight_dfs, "SAMI 2", "SAMI 2")

# Calculate for "PAI 2"
functs.calculate_averages_and_failures(cs15_df, flight_dfs, "PAI 2", "PAI 2")

#top_three_ami1_infractions = functs.get_top_column_titles_with_most_xs(ami1_df)
#print("The top three infractions for AMI 1 are:")
#print(top_three_ami1_infractions)

#top_three_ami2_infractions = functs.get_top_column_titles_with_most_xs(ami2_df)
#print("The top five infractions for AMI 2 are:")
#print(top_three_ami2_infractions)

top_three_ami3_infractions = functs.get_top_column_titles_with_most_xs(ami3_df)
print("The top five infractions for AMI 3 are:")
print(top_three_ami3_infractions)

top_three_sami2_infractions = functs.get_top_column_titles_with_most_xs(sami2_df)
print("The top five infractions for SAMI 2 are:")
print(top_three_sami2_infractions)

top_three_pai2_infractions = functs.get_top_column_titles_with_most_xs(pai2_df)
print("The top five infractions for PAI 2 are:")
print(top_three_pai2_infractions)

#failures = functs.get_ktest_fails(ktest_df, "Spring K-Test #1 (January 22, 2025) [Total Pts: 35 Percentage] |393089")
#for name, count in failures.items():
    #print(f"{name} failed the most recent ktest and {count} previous ktests.")

#functs.get_ktest_averages(ktest_df, flight_dfs, "Spring K-Test #1 (January 22, 2025) [Total Pts: 35 Percentage] |393089")

#scouting_report_ami1 = functs.get_top_column_titles_with_most_xs(othersq_ami_1)
#print("The top five AMI 1 infractions for CS-28 Scouting Report are:")
#print(scouting_report_ami1)
#print("The average of the squadron they graded was: ", othersq_ami_1["Score"].mean())

#scouting_report_ami_2 = functs.get_top_column_titles_with_most_xs(othersq_ami_2)
#print("The top five AMI 2 infractions for CS-28 Scouting Report are:")
#print(scouting_report_ami_2)
#print("The average of the squadron they graded was: ", othersq_ami_2["Score"].mean())