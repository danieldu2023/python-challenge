# PyBank Analysis 
import csv 
import os 

# Set file path
csvpath = os.path.join('Resources','budget_data.csv')

month = 0
total = 0
current_amount = 0
change_in_month = 0
average_change = 0
total_change_in_PF = 0

change_PL = { month:[month] , change_in_month:[change_in_month] }



# Open the CSV using the UTF-8 encoding
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(csvreader)


# Print out all the rows
    for row in csvreader:
        month = month + 1
        total = total + int(row[1])
        change_in_month = int(row[1]) - current_amount
        print(change_in_month)
        current_amount = int(row[1])
        total_change_in_PF = total_change_in_PF + change_in_month


print("/////////")
print(total_change_in_PF)
print(month)      
average_change = total_change_in_PF / month 

        # print(row)
    
# Total number of months included in the dataset
    # print(f"Total Month : {month}")
    # print(f"Total : {total}")
    # print(change_in_month)
print(average_change)

print(change_PL)