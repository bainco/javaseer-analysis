import subprocess
from subprocess import call


def RecreateRuntimeErrors(theProgramName, theProgram):

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
    proc = subprocess.Popen(["java", program_compiled_name],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_value, stderr_value = proc.communicate('through stdin to stdout')
    #print '\tpass through:', repr(stdout_value)
    #print 'stderr:', repr(stderr_value)

    # Remove the uncompiled version
    call(["rm", program_name])
    # Remove the compiled version
    call(["rm", program_compiled_name + ".class"])

    # Retrun any errors we had
    return stderr_value
