import os
import csv

bankinfo=os.path.join(".","budget_data.csv")
out_filename=os.path.join(".","Fin_analysis.txt")

month=[]
profit_loss=[]

#The format output function is both the cli out and the file write formats
def format_output(total_months, total, avg_change, great_month, greatest_increase, min_month,greatest_decrease):
    analysis=  (f"Financial Analysis\n"
                f"----------------------------\n"
                f"Total Months: {total_months}\n"
                f"Total: ${int(total)}\n"
                f"Average  Change: ${int(avg_change)}\n"
                f"Greatest Increase in Profits: {great_month} (${int(greatest_increase)})\n"
                f"Greatest Decrease in Profits: {min_month} (${int(greatest_decrease)})\n"
                )
    return analysis

with open(bankinfo, "r" ,newline='') as inputfile:
    bank_csv= csv.reader(inputfile)
    #this next skips the first line so that they're not appended to the lists  
    next(bank_csv)
    #add the contents of the csv into a list
    for row in bank_csv:
        month.append(row[0])
        profit_loss.append(float(row[1]))

period=len(month)
totals=sum(profit_loss)
averages=totals/period
maximum=max(profit_loss)
max_month=month[profit_loss.index(max(profit_loss))]
minimum=min(profit_loss)
min_month=month[profit_loss.index(min(profit_loss))]

print(format_output(period,totals,averages,max_month,maximum, min_month,minimum))

with open(out_filename, "w" ) as output:
    output.write(f"{format_output(period,totals,averages,max_month,maximum, min_month,minimum)}")

