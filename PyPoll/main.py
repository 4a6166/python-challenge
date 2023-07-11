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

for i in range(0, len(candidates)):
    print(
        candidates[i] + ":",
        str(round(100 * votes[i]/votesTotal, 3)) + "%",
        '(' + str(votes[i]) + ')'
        )


# Results string for use in console print and writer
result = f"""Election Results
-------------------------
Total Votes: {votesTotal}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette:
Raymon Anthony Doane:
-------------------------
Winner: {winner}
-------------------------
"""

# Print results
print(result)

# # writer
# with open(writePath, 'w') as writeFile:
#     writeFile.write(result)
