import subprocess
from subprocess import call
import csv


STUDENT_ID_INDEX = 0
CONDITION_INDEX = 1
JAVAC_CALL_INDEX = 2
ASSIGNMENT_NAME_INDEX = 3
TIME_STAMP_INDEX = 4
WEEK_NUM_INDEX = 5
PROGRAM_INDEX = 6


def RunAllPrograms():

    successes_by_student = {}
    with open("runtime_tests.csv", "rb") as f:
        reader = csv.reader(f)
        headers = reader.next()
        print "Processing..."
        for i, line in enumerate(reader):
            #print 'line[{}] = {}'.format(i, line)
            loadStudentID  = str(line[STUDENT_ID_INDEX])
            loadCondition = str(line[CONDITION_INDEX])
            loadJavacCall = str(line[JAVAC_CALL_INDEX])
            loadAssignment = str(line[ASSIGNMENT_NAME_INDEX])
            loadTimestamp  = str(line[TIME_STAMP_INDEX])
            loadWeekNum = str(line[WEEK_NUM_INDEX])
            loadProgram = str(line[PROGRAM_INDEX])

            success_entry = {'studentid':loadStudentID,'condition':loadCondition, 'javac_call':loadJavacCall, 'assignment_name':loadAssignment, 'timestamp':loadTimestamp, 'week_num':loadWeekNum, 'program':loadProgram}
            if loadStudentID in successes_by_student:
                successes_by_student[loadStudentID].append(success_entry)
            else:
                successes_by_student[loadStudentID] = [success_entry]

    for key, value in successes_by_student.iteritems():
        for entry in value:
            runtimeErrors = RecreateRuntimeErrors(entry['javac_call'], entry['program'])
            entry['runtime_errors'] = runtimeErrors

    fieldnames = ['studentid', 'condition', 'javac_call', 'assignment_name', 'timestamp','week_num', 'program', 'runtime_errors']
    with open("runtime-test-results", 'wb') as outfile:
        w = csv.DictWriter(outfile, fieldnames=fieldnames)
        w.writeheader()
        for key,val in successes_by_student.items():
            for item in val:
                w.writerow(item)

def RecreateRuntimeErrors(theProgramName, theProgram):

    print theProgramName
    # Go ahead and generate the compiled name
    theProgramCompiledName = theProgramName.replace(".java", "")

    # Create a text file with the correct name
    text_file = open(theProgramName, "w")
    # Insert the program
    text_file.write(theProgram)
    # Close the file
    text_file.close()

    # Compile the program
    call(["javac", theProgramName])

    # Run the program and listen for errors
    proc = subprocess.Popen(["java", theProgramCompiledName],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_value, stderr_value = proc.communicate('through stdin to stdout')
    #print '\tpass through:', repr(stdout_value)
    #print 'stderr:', repr(stderr_value)

    # Remove the uncompiled version
    call(["rm", theProgramName])
    # Remove the compiled version
    call(["rm", theProgramCompiledName + ".class"])

    # Retrun any errors we had
    return repr(stderr_value)
