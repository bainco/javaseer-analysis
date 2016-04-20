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

    # Missing parenthesis or bracket
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

    # variable not intialized
    if re.search("variable .* might not have been initialized$", theError):
        return "variable not intialized"

    # Type issues
    if re.search("incompatible types: (.*)", theError):
        return "type mismatch"
    if re.search("incomparable types: (.*)", theError):
        return "type mismatch"

    return theError
