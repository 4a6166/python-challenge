# All paths are from the python-challenge dir
# From python-challenge run `py PyBank/main.py`

import os
import csv

# declare empty vars
totalMonths = 0
netPL = 0

plPrev = None
changesPL = []
avgPL = 0
increasePLGreatest = ['date', '0']  # date, amount
decreasePLGreatest = ['date', '0']  # date, amount

# Reader
csvPath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Assign first row of CSV as header
    csvHeader = next(csvReader)

    for row in csvReader:
        date = row[0]
        pl = int(row[1])  # all values in data are whole numbers

        totalMonths += 1
        netPL += pl

        if plPrev is not None:
            changesPL.append(pl - plPrev)

        plPrev = pl

#        # Conditionals for greatest increase/decrease
#        if pl > int(increasePLGreatest[1]):
#            increasePLGreatest = row
#        elif pl < int(decreasePLGreatest[1]):
#            decreasePLGreatest = row

avgPL = round(sum(changesPL) / len(changesPL), 2)

# Results strings
result = f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${netPL}
Average Change: ${avgPL}
Greatest Increase in Profits: {increasePLGreatest[0]} ({increasePLGreatest[1]})
Greatest Decrease in Profits: {decreasePLGreatest[0]} ({decreasePLGreatest[1]})
"""

# Print results
print(result)

# Write results to analysis folder
# TODO: set up writer, write to PyBank/analysis/result.txt
