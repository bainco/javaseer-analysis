execfile("IDtoCondition.py")
# This loads in the IDtoCondition CSV file into two dictionaries
# 1. The IDtoConditionDictionary
# 2. the IDtoRunsDictionary

execfile("error_identifier.py")
execfile("assignment_identifier.py")
execfile("errors_reader.py")
execfile("TimeDiff.py")

print "done."

# This process the DB dump.csv into a bunch of dictionaries

AllStudentsToCSV("run_output.csv")
