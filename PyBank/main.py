# All paths are from the python-challenge dir
# From python-challenge run `py PyBank/main.py`

import os
import csv

# declare empty vars
totalMonths = 0
netPL = 0

plPrev = None
changes = {}
avgPL = 0
increasePLGreatest = ['date', '0']
decreasePLGreatest = ['date', '0']

# file paths
csvPath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
writePath = os.path.join('PyBank', 'analysis', 'result.txt')

# reader
with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Assign first row of CSV as header, pop it from rows list
    csvHeader = next(csvReader)

    for row in csvReader:
        date = row[0]
        pl = int(row[1])  # all values in data are whole numbers

        # Add row count and pl to totals
        totalMonths += 1
        netPL += pl

        # Add PL change to array
        if plPrev is not None:
            changePl = pl - plPrev
            changes[date] = changePl

        # Track PL for next row's change calc
        plPrev = pl

# Logic for average profit and loss calculation
avgPL = round(sum(changes.values())/len(changes), 2)

# Assigns date and amount to greatest increase and decrease variables
increasePLGreatest[1] = max(changes.values())
increasePLGreatest[0] = max(changes, key=changes.get)

decreasePLGreatest[1] = min(changes.values())
decreasePLGreatest[0] = min(changes, key=changes.get)

# Results string for use in console print and writer
result = f"""Financial Analysis
----------------------------
Total Months: {totalMonths}
Total: ${netPL}
Average Change: ${avgPL}
Greatest Increase in Profits: {increasePLGreatest[0]} (${increasePLGreatest[1]})
Greatest Decrease in Profits: {decreasePLGreatest[0]} (${decreasePLGreatest[1]})"""

# Print results
print(result)

# writer
with open(writePath, 'w') as writeFile:
    writeFile.write(result)
