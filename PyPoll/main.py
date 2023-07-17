# All paths are from the python-challenge dir
# From python-challenge run `py PyPoll/main.py`

import os
import csv

# declare empty vars
candidates = {}

# file paths
csvPath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
writePath = os.path.join('PyPoll', 'analysis', 'result.txt')

# reader
with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Assign first row of CSV as header, pop it from rows list
    csvHeader = next(csvReader)  # Ballot ID,County,Candidate

    for row in csvReader:
        try:
            candidates[row[2]] += 1
        except:
            candidates[row[2]] = 1

# var to hold candidate info to be concatenated into result string
totCount = sum(candidates.values())
resultBody = ""
for candidate in candidates:
    percent = round(100 * candidates[candidate]/totCount, 3)
    resultBody = resultBody + f'\n{candidate}: {percent}% ({candidates[candidate]})'
 
# Results string for use in console print and writer
resultHead = f"""Election Results
-------------------------
Total Votes: {totCount}
-------------------------"""

resultTail = f"""
-------------------------
Winner: {max(candidates, key=candidates.get)}
-------------------------
"""

result = resultHead + resultBody + resultTail

# Print results
print(result)

# writer
with open(writePath, 'w') as writeFile:
    writeFile.write(result)
