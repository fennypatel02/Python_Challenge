
# Import Dependencies
import os
import csv 

# Set path for file
budget_data = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Analysis" , "pybank.txt")

#read the data from the file
with open(budget_data, newline="", encoding="utf-8") as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print(f" {csv_header}")


# find net amount of profit and loss
    Profit = []
    months = []

# read each row of data after header
    for rows in csv_reader:
            Profit.append(int(rows[1]))
            months.append(rows[0])

    # find revenue change
    average_change =[]

    for row in range(1, len(Profit)):
        average_change.append((int(Profit[row]) - int(Profit[row-1])))
        
   # calculate total length of months
    total_months = len(months)
    
    # calculate average revenue change
    revenue_average_change = sum(average_change) / len(average_change)
    revenue_average = round(revenue_average_change, 2)
    
    # greatest increase in revenue
    greatest_increase = max(average_change)
    #greatest decrease in revenue
    greatest_decrease = min(average_change)
    
    #greatest increse in month
    greatest_increase_month = months[average_change.index(max(average_change))+1]
    greatest_decrease_month = months[average_change.index(min(average_change))+1]


#output requireed
print("Financial Analysis")
print("-----------------------------------")
print("Total months: " + str(total_months))
print("Total: $" + str(sum(Profit)))
print("Average change: $" + str(revenue_average))
print(f"Greatest Increase in Profits: {str(greatest_increase_month)} $({str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} $({str(greatest_decrease)})")


with open (outputfile, "w") as file:
    file.write ("Financial Analysis \n")
    file.write("----------------------------------- \n")
    file.write("Total months: " + str(total_months) )
    file.write("\n Total: $" + str(sum(Profit)))
    file.write("\n Average change: $" + str(revenue_average))
    file.write(f"\nGreatest Increase in Profits: {str(greatest_increase_month)} $({str(greatest_increase)})")
    file.write(f"\nGreatest Decrease in Profits: {str(greatest_decrease_month)} $({str(greatest_decrease)})")




