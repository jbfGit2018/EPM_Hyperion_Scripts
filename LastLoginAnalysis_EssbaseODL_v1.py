import re
import csv

# Open the log file
with open('C:\\Users\\John French\\Documents\\Essbase_ODL logs (3)\\Essbase logs\\E drive\\ESSBASE_ODL.log', 'r') as file:
    log_data = file.readlines()

# Create a dictionary to store the last login date for each user ID
last_login_dates = {}


# Define the pattern to search for
pattern = r'\[(.*?)\].*?Logging in user \[(.*?)\]'

# Search for the pattern in each line and update the last login date for each user ID
for line in log_data:
    match = re.search(pattern, line)
    if match:
        date = match.group(1)
        user_id = match.group(2)
        last_login_dates[user_id] = date

# Open the CSV file for writing
with open('output2.csv', mode='w', newline='') as csv_file:
    fieldnames = ['User ID', 'Last Login Date']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Write the last login date for each user ID to the CSV file
    for user_id, last_login_date in last_login_dates.items():
        writer.writerow({'User ID': user_id, 'Last Login Date': last_login_date})
