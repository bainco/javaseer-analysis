execfile("IDtoCondition.py")
# This loads in the IDtoCondition CSV file into two dictionaries
# 1. The IDtoConditionDictionary
# 2. the IDtoRunsDictionary

execfile("error_identifier.py")
execfile("errors_reader.py")
# This process the DB dump.csv into a bunch of dictionaries

AllStudentsToCSV("process_ouput.csv")
