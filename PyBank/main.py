import os
import csv

file = os.path.join("Resources","Budget.csv")

months_total = 0
profit_total = 0
profit_new = 0
profit_previous = 0
profit_change = 0
profitlist = []
profit_average = 0
profit_max = 0
profit_min = 0

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        months_total = months_total + 1

        profit_total = profit_total + int(row[1])

        profit_new =  int(row[1])
        profit_change = profit_new - profit_previous
        profitlist.append(profit_change)
        profit_previous = profit_change
        profit_average = (sum(profitlist) / months_total)
        profit_average = round(profit_average, 2)

        if profit_new > profit_max:
            profit_max = profit_change
            month_max = row[0]
        
        if profit_new < profit_min:
            profit_min = profit_change
            month_min = row[0]
    
    

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months_total}")
    print(f"Total Profit: ${profit_total}")
    print(f"Average Change: ${profit_average}")
    print(f"Greatest Increase in Profits: {month_max} ${profit_max}")
    print(f"Greatest Decrease in Profits: {month_min} ${profit_min}")

    analysisfile = os.path.join("analysis/analysis.txt")
    
    analysis = open(analysisfile,"w")

    analysis.write("Financial Analysis of Profit/Loss PyBank \n")
    analysis.write("---------------------------- \n")
    analysis.write(f"Total Months: {months_total} \n")
    analysis.write(f"Total Profit: ${profit_total} \n")
    analysis.write(f"Average Change: ${profit_average} \n")
    analysis.write(f"Greatest Increase in Profits: {month_max} ${profit_max} \n")
    analysis.write(f"Greatest Decrease in Profits: {month_min} ${profit_min} \n")
    analysis.write(f"Thank you for your attention. Now go. Go make our biggest Increase bigger than our biggest Decrease!")