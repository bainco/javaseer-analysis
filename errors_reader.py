import csv

JAVASEER_INDEX = 0
STUDENT_ID_INDEX = 1
JAVAC_CALL_INDEX = 2
TIME_STAMP_INDEX = 3
JAVA_PROGRAM_INDEX = 4
JAVAC_OUT_INDEX = 5

# Read in the CSV File and grab all of the errors

#Student Dictionary
errors_by_student = dict()

#Assignment Dictionary
errors_by_assignment = dict()


print "Opening File..."
# Stick them in errorList
with open("test_output.csv", "rb") as f:
    reader = csv.reader(f)
    print "Processing..."
    for i, line in enumerate(reader):
        #print 'line[{}] = {}'.format(i, line)
        loadStudentID  = str(line[STUDENT_ID_INDEX])
        loadAssignment = str(line[JAVAC_CALL_INDEX])
        loadTimestamp  = str(line[TIME_STAMP_INDEX])
        loadError = str(line[JAVAC_OUT_INDEX])
        
        #print "StudentID: " + loadStudentID
        #print "Assignment: " + loadAssignment
        #print "Timestamp: " + loadTimestamp
        #print "Error: " + loadError
        
        # Iterate through all the lines of each error and look for 'error: '
        for error_line in loadError.splitlines():
            if error_line.find("error: ") != -1:
                process_error = error_line.split("error: ")
                error_type = process_error[-1]
                
                # Create a new dictionary for this error
                error_entry = {'error':error_type, 'studentid':loadStudentID, 'assignment':loadAssignment, 'timestamp':loadTimestamp}
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










