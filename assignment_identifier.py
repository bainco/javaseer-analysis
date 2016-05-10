import re

def AssignmentIdentifier(theAssignment):

    if theAssignment.lower().find("image") != -1:
        if theAssignment.lower().find("vote") == -1:
            if theAssignment.lower().find("voting") == -1:
                if theAssignment.lower().find("election") == -1:
                    return "Image"

    if theAssignment.lower().find("age") != -1:
        return "age"

    if theAssignment.lower().find("hello") != -1:
        return "Hello World"

    if theAssignment.lower().find("elephantexam") != -1:
        return "ElephantExam"
    if theAssignment.lower().find("elephat") != -1:
        return "ElephantExam"
    if theAssignment.lower().find("elephant") != -1:
        return "ElephantExam"

    if theAssignment.lower().find("scanner") != -1:
        return "Scanner"

    if theAssignment.lower().find("practicelab") != -1:
        return "Practice Lab"

    if theAssignment.lower().find("airline") != -1:
        return "Airline"

    if theAssignment.lower().find("testscore") != -1:
        return "Test Score"

    if (theAssignment.lower().find("party") != -1) or (theAssignment.lower().find("birthday") != -1):
        return "Birthday"

    if (theAssignment.lower().find("rectangle") != -1):
        return "Rectangle/Turkey"
    if (theAssignment.lower().find("turkey") != -1):
        return "Rectangle/Turkey"

    # Election / Age Assignment
    if theAssignment.lower().find("vote") != -1:
        return "Election"
    if theAssignment.lower().find("voting") != -1:
        return "Election"
    if (theAssignment.lower().find("election") != -1):
        return "Election"

    # JOption
    if theAssignment.lower().find("joption") != -1:
        return "JOption"

    # YES/NO = SHOE
    if theAssignment.lower().find("online") != -1:
        return "Shoe Buying"
    if theAssignment.lower().find("shoe") != -1:
        return "Shoe Buying"
    if theAssignment.lower().find("sneaker") != -1:
        return "Shoe Buying"
    if theAssignment.lower().find("yesno") != -1:
        return "Shoe Buying"

    return theAssignment
