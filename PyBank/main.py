import os
import csv
from statistics import mean

# Variables
budget_data = os.path.join('Resources', 'budget_data.csv')
revenue_data = []           # monthly revenue data
month_data = []             # month revenues realized
monthly_change = []         # month-to-month change
text_output = []                  # stuff to print


# grab data from CSV file using horrible I/O function
with open(budget_data, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        for row in csvreader:
            month_data.append(str(row[0]))
            revenue_data.append(float(row[1]))


# create 'monthly_change' list 
total_months = len(revenue_data)
second_month = 1
for month in range(second_month,total_months):
    monthly_change.append(revenue_data[month] - revenue_data[month-1])
    

# make month_name and monthly_change have same index 
month_data.pop(0)


# calculate variables of interest
total = "${:,.2f}".format(sum(revenue_data))
average_change = "${:,.2f}".format(mean(monthly_change))
greatest_increase = "${:,.2f}".format(max(monthly_change))
gi_month = month_data[monthly_change.index(max(monthly_change))]
greatest_decrease = "${:,.2f}".format(min(monthly_change))
gd_month = month_data[monthly_change.index(min(monthly_change))]


# print output
text_output.append("Financial Analysis")
text_output.append("-------------------------\n")
text_output.append("Total Months: " + str(total_months))
text_output.append("Total: " + str(total))
text_output.append("Average Change: " + str(average_change))
text_output.append("Greatest Increase In Profits: " + str(gi_month) + "  (" + str(greatest_increase) + ")")
text_output.append("Greatest Decrease In Profits: " + str(gd_month) + "  (" + str(greatest_decrease) + ")")

for line in text_output:
    print(line)

outpath = os.path.join('Analysis', 'MyFile.txt')
file_object = open(outpath, "a")
for line in text_output:
    file_object.write(line)
    file_object.write("\n")
file_object.close()




