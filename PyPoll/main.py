# All paths are from the python-challenge dir
# From python-challenge run `py PyPoll/main.py`

import os
import csv

# declare empty vars
votesTotal = 0
candidates = []
percetages = []
votes = []
winner = ""

# file paths
csvPath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
writePath = os.path.join('PyPoll', 'analysis', 'result.txt')

# reader
with open(csvPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    # Assign first row of CSV as header, pop it from rows list
    csvHeader = next(csvReader)

    for row in csvReader:
        # iterate vote count
        votesTotal += 1

        if row[2] in candidates:
            # get index that matches all lists
            i = candidates.index(row[2])
            # increment votes count
            votes[i] += 1
        else:
            # add candidate to list
            candidates.append(row[2])
            # add new vote index, counting this row as first vote
            votes.append(1)

# var to hold candidate info to be concatenated into result string
resultBody = ""

# loop over candidate list to index into totals list and produce string of results
# for i in range(0, len(candidates)):
#     percent = str(round(100 * votes[i]/votesTotal, 3))
#     candidateString = "\n" + candidates[i] + ": " + percent + "% " + '(' + str(votes[i]) + ')'
#     resultBody += candidateString

# alt lookup using enumerate()
for index, candidate in enumerate(candidates):
    percent = str(round(100 * votes[index]/votesTotal, 3))
    candidateString = "\n" + candidates[index] + ": " + percent + "% " + '(' + str(votes[index]) + ')'
    resultBody += candidateString

# determine winner
winner = candidates[votes.index(max(votes))]

# Results string for use in console print and writer
resultHead = f"""Election Results
-------------------------
Total Votes: {votesTotal}
-------------------------"""

resultTail = f"""
-------------------------
Winner: {winner}
-------------------------
"""

result = resultHead + resultBody + resultTail

# Print results
print(result)

# writer
with open(writePath, 'w') as writeFile:
    writeFile.write(result)
