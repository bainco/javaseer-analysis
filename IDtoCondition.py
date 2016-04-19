import csv

# Needs to:
#   1. Read in the CSV file with the id to condition map
#   2. Create a dicitionary where each entry is an id, condition code pair

ID_INDEX = 0
RUNS_INDEX = 1
CONDITION_INDEX = 2
CONDITION_CODE_INDEX = 3

# Maps studentID to condition
IDtoConditionDictionary = {}

# Maps studentID to num of runs
IDtoRunsDictionary = {}

print "Opening ID to Condition file..."

with open("IDtoCondition.csv", "rb") as f:
    reader = csv.reader(f)
    headers = reader.next()
    print "Processing..."
    for i, line in enumerate(reader):
        loadStudentID = str(line[ID_INDEX])
        loadRuns = int(line[RUNS_INDEX])
        loadCondition = str(line[CONDITION_INDEX])
        loadConditionCode = int(line[CONDITION_CODE_INDEX])

        IDtoConditionDictionary[loadStudentID] = loadCondition
        IDtoRunsDictionary[loadStudentID] = loadRuns
