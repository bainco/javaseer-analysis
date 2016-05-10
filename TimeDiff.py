from copy import *
from operator import itemgetter
import datetime
# errors_by_student
# successes_by_student
#
#
# error_entry = {'error_type': loadErrorType, 'error_message':loadErrorMessage, 'studentid':loadStudentID,'condition':loadStudentCondition, 'assignment':loadAssignment, 'assignment_name':assignmentName, 'timestamp':loadTimestamp, 'week_num':str(weekCounter)}
# success_entry = {'studentid':loadStudentID,'condition':loadStudentCondition, 'assignment':loadAssignment, 'assignment_name':assignmentName, 'timestamp':loadTimestamp, 'week_num':str(weekCounter)}
time_format = '%Y-%m-%d %H:%M:%S.%f'

all_comps_by_student = deepcopy(errors_by_student)

for key, value in successes_by_student.iteritems():
    all_comps_by_student[key] = all_comps_by_student[key] + deepcopy(value)
    for item in all_comps_by_student[key]:
        item['timestamp'] = datetime.datetime.strptime(item['timestamp'][:-3], time_format)

for key, value in all_comps_by_student.iteritems():
    all_comps_by_student[key] = sorted(value, key=itemgetter('timestamp'))

    currentAssignment = ""
    prevTime = 0
    for item in value:
        loadedTime = deepcopy(item['timestamp'])

        if item['assignment'] != currentAssignment:
            #print loadedTime
            #print item['assignment']
            #print "vs"
            #print currentAssignment
            currentAssignment = deepcopy(item['assignment'])
            item['timeDelta'] = 0

        else:
            timeDiff = (loadedTime - prevTime).total_seconds()
            if timeDiff == 0:
                item['timeDelta'] = -1
            else:
                item['timeDelta'] = timeDiff

        prevTime = deepcopy(loadedTime)

for key, value in all_comps_by_student.iteritems():
    all_comps_by_student[key] = [v for v in all_comps_by_student[key] if v['timeDelta'] != -1]

for key, value in all_comps_by_student.iteritems():
    all_comps_by_student[key] = sorted(value, key=itemgetter('timestamp'))
    currentAssignment = ""
    for item in value:
        loadedTime = deepcopy(item['timestamp'])

        if item['assignment'] != currentAssignment:
            currentAssignment = deepcopy(item['assignment'])
            firstTime = deepcopy(loadedTime)
            item['timeSinceStart'] = 0
            item['timeDelta'] = 0

        else:
            item['timeDelta'] = (loadedTime - prevTime).total_seconds()
            item['timeSinceStart'] = (loadedTime - firstTime).total_seconds()

        prevTime = loadedTime

for key, value in all_comps_by_student.iteritems():
    all_comps_by_student[key] = sorted(all_comps_by_student[key], key=itemgetter('timestamp'))
