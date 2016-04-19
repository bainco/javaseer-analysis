import csv
import re
import datetime

JAVASEER_INDEX = 0
STUDENT_ID_INDEX = 1
JAVAC_CALL_INDEX = 2
TIME_STAMP_INDEX = 3
JAVA_PROGRAM_INDEX = 4
JAVAC_OUT_INDEX = 5

time_format = '%Y-%m-%d %H:%M:%S.%f'

thisMonday = datetime.datetime(2015, 10, 12) # October 12, 2015
nextMonday = thisMonday + datetime.timedelta(days=7)
weekCounter = 0

# Read in the CSV File and grab all of the errors

#Student Dictionary
errors_by_student = dict()

#Assignment Dictionary
errors_by_assignment = dict()

print "Opening File..."
# Stick them in errorList
with open("oas_javaseer-dump.csv", "rb") as f:
    reader = csv.reader(f)
    headers = reader.next()
    print "Processing..."
    for i, line in enumerate(reader):
        #print 'line[{}] = {}'.format(i, line)
        loadStudentID  = str(line[STUDENT_ID_INDEX])
        loadAssignment = str(line[JAVAC_CALL_INDEX])
        loadTimestamp  = str(line[TIME_STAMP_INDEX])
        loadError = str(line[JAVAC_OUT_INDEX])

        if IDtoConditionDictionary[loadStudentID] == "IGNORE":
            print "Omitted " + str(loadStudentID) + " b/c IGNORE"
            continue
        if IDtoRunsDictionary[loadStudentID] < 5:
            print "Omitted " + str(loadStudentID) + " b/c < 5 runs"
            continue

        #print "StudentID: " + loadStudentID
        #print "Assignment: " + loadAssignment
        #print "Timestamp: " + loadTimestamp
        #print "Error: " + loadError

        # Iterate through all the lines of each error and look for 'error: '
        #errorCount = 0
        for error_line in loadError.splitlines():

            #if len(re.findall(r'\d+ errors?$', error_line)) > 0:
            #    if errorCount != int(re.findall('\d+', re.findall(r'\d+ errors?$', error_line)[0])[0]):
            #        print error_line
            #        print errorCount
                # This is the number of errors from that line

            if error_line.find("error: ") != -1:
                #errorCount += 1
                process_error = error_line.split("error: ")
                error_type = process_error[-1]

                loadedTime = datetime.datetime.strptime(loadTimestamp[:-3], time_format)

                if (loadedTime > nextMonday):
                    while (loadedTime > nextMonday):
                        thisMonday = nextMonday
                        nextMonday = nextMonday + datetime.timedelta(days=7)
                    weekCounter += 1

                # Create a new dictionary for this error
                error_entry = {'error':error_type, 'studentid':loadStudentID, 'assignment':loadAssignment, 'timestamp':loadTimestamp, 'week_num':str(weekCounter)}

              # Check to see if we've seen this student before
                # If so, just append the new error_entry to the list of dicts for that student
                # Otherwise, make a new list
                if loadStudentID in errors_by_student:
                    errors_by_student[loadStudentID].append(error_entry)
                else:
                    errors_by_student[loadStudentID] = [error_entry]

                #Check to see if we've seen this assignment before
                # If so, just append the new error_entry to the list of dicts for that asssignment
                # Otherwise, make a new list
                if loadAssignment in errors_by_assignment:
                    errors_by_assignment[loadAssignment].append(error_entry)
                else:
                    errors_by_assignment[loadAssignment] = [error_entry]
print "done."

def StudentToCSV(theStudent):
""" Takes in a studentID (string) and outputs all of that students errors
 to a CSV file with the name 'studentID'.csv """"
    writeToCSV(str(theStudent), str(theStudent) + '.csv')

def writeToCSV (theList, fileName):
   " Prints the contents of a list of dictionaries to a CSV file where each row is a dictionary "
   with open(fileName, 'wb') as outfile:
      w = csv.DictWriter(outfile, theList[0].keys())
      w.writeheader()
      for item in theList:
         w.writerow(item)
