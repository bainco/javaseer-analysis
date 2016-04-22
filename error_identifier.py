import re

def ErrorTypeIdentifier(theError):
    # Incorrect javac call (missing .java)
    if re.search("Class names, '.*', are only accepted if annotation processing is explicitly requested", theError):
        return "incorrect javac call"
    if re.search("javac: file not found: (.*)\.java", theError):
        return "incorrect javac call"
    if re.search("javac: invalid flag: (.*)$", theError):
        return "incorrect javac call"

    # Class name does not match file name
    if re.search("class .* is public, should be declared in a file named .*\.java$", theError):
        return "wrong file/class name"

    # Incorrect package import
    if re.search("package (.*) does not exist$", theError):
        return "wrong package name"

    # Missing parenthesis or bracket
    if theError == "\']\' expected":
        return "unmatched parenthesis or bracket"
    if re.search("\'\(\' or \'\[\' expected", theError):
        return "unmatched parenthesis or bracket"
    if re.search("\'\)\' expected", theError):
        return "unmatched parenthesis or bracket"
    if theError == "'(' expected":
        return "unmatched parenthesis or bracket"

    # Missing curly brace
    if re.search("reached end of file while parsing", theError):
        return "missing curly brace"
    if re.search("\'{\' expected", theError):
        return "missing curly brace"

    # illegal escape characters
    if theError == "illegal character: '\'":
        return "illegal escape character"
    if theError == "illegal escape character":
        return "illegal escape character"

    # copy and pasted smart quotes
    if theError == "illegal character: '\u201d'":
        return "used smart quotes"
    if theError == "illegal character: '\u201c'":
        return "used smart quotes"

    # variable already defined
    if re.search("variable (.*) is already defined in method (.*)$", theError):
        return "variable already defined"

    # variable not intialized
    if re.search("variable .* might not have been initialized$", theError):
        return "variable not intialized"
    if theError == "variable not intialized":
        return "variable not initialized"

    # Static / Context issues
    if re.search("Illegal static declaration in inner class (.*)$", theError):
        return "static context issues"
    if re.search("non-static method (.*) cannot be referenced from a static context$", theError):
        return "static context issues"
    if re.search("non-static variable (.*) cannot be referenced from a static context$", theError):
        return "static context issues"

    # Type issues
    if re.search("incompatible types: (.*)", theError):
        return "type mismatch"
    if re.search("incomparable types: (.*)", theError):
        return "type mismatch"
    if re.search("bad operand types for binary operator '(.*)'$", theError):
        return "type mismatch"
    if re.search("bad operand type (.*) for unary operator '(.*)'$", theError):
        return "type mismatch"

    # Method argument issues
    if re.search("no suitable method found for (.*)$", theError):
        return "wrong arguments"
    if re.search("no suitable constructor found for (.*)$", theError):
        return "wrong arguments"
    if re.search("constructor (.*) in class (.*) cannot be applied to given types;$", theError):
        return "wrong arguments"

    return theError
