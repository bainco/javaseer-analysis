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

#successful compilations Dictionary
successes_by_student = dict()

print "Opening oas_javaseer-dump..."
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

        loadStudentCondition = str(IDtoConditionDictionary[loadStudentID])
        #print "StudentID: " + loadStudentID
        #print "Assignment: " + loadAssignment
        #print "Timestamp: " + loadTimestamp
        #print "Error: " + loadError
        assignmentName = AssignmentIdentifier(loadAssignment)

        loadedTime = datetime.datetime.strptime(loadTimestamp[:-3], time_format)

        if (loadedTime > nextMonday):
            while (loadedTime > nextMonday):
                thisMonday = nextMonday
                nextMonday = nextMonday + datetime.timedelta(days=7)
            weekCounter += 1

        if loadError == "":
            # Create a new dictionary for this error
            success_entry = {'studentid':loadStudentID,'condition':loadStudentCondition, 'assignment':loadAssignment, 'timestamp':loadTimestamp, 'week_num':str(weekCounter)}
            if loadStudentID in successes_by_student:
                successes_by_student[loadStudentID].append(success_entry)
            else:
                successes_by_student[loadStudentID] = [success_entry]

        # Iterate through all the lines of each error and look for 'error: '
        #errorCount = 0
        for error_line in loadError.splitlines():

            #if len(re.findall(r'\d+ errors?$', error_line)) > 0:
            #    if errorCount != int(re.findall('\d+', re.findall(r'\d+ errors?$', error_line)[0])[0]):
            #        print error_line
            #        print errorCount
            # This is the number of errors from that line
            if (error_line.find("error: ") != -1) or (error_line.find("javac: ") != -1):
                #errorCount += 1

                if error_line.find("error: ") != -1:
                    process_error = error_line.split("error: ")
                    loadErrorMessage = process_error[-1]
                elif error_line.find("javac: ") != -1:
                    loadErrorMessage = error_line

                loadErrorType = ErrorTypeIdentifier(loadErrorMessage)

                # Create a new dictionary for this error
                error_entry = {'error_type': loadErrorType, 'error_message':loadErrorMessage, 'studentid':loadStudentID,'condition':loadStudentCondition, 'assignment':loadAssignment, 'timestamp':loadTimestamp, 'week_num':str(weekCounter)}

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

def AllStudentsToCSV(fileName):

    fieldnames = ['studentid', 'condition', 'assignment', 'error_type', 'error_message', 'timestamp','week_num']
    with open("errors-" + fileName, 'wb') as outfile:
       w = csv.DictWriter(outfile, fieldnames=fieldnames)
       w.writeheader()
       for key,val in errors_by_student.items():
           for item in val:
               w.writerow(item)

    fieldnames = ['studentid','condition', 'assignment', 'timestamp', 'week_num']
    with open("successes-" + fileName, 'wb') as outfile:
        w = csv.DictWriter(outfile, fieldnames=fieldnames)
        w.writeheader()
        for key,val in successes_by_student.items():
            for item in val:
                w.writerow(item)

def StudentToCSV(theStudent):
    # Takes in a studentID (string) and outputs all of that students errors to a CSV file with the name studentID.csv
    if str(theStudent) in errors_by_student:
        print "Writing all errors for " + theStudent + " to csv."
        writeToCSV(errors_by_student[str(theStudent)], str(theStudent) + '.csv')
        print "done."
    else:
        print "No student with ID " + theStudent + " found in the dictionary."


def writeToCSV (theList, fileName):
   " Prints the contents of a list of dictionaries to a CSV file where each row is a dictionary "
   with open(fileName, 'wb') as outfile:
      w = csv.DictWriter(outfile, theList[0].keys())
      w.writeheader()
      for item in theList:
         w.writerow(item)
