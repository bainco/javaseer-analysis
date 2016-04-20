import subprocess
from subprocess import call

# I can grab this from the program column!
loadProgram = """
public class HelloPrinter
{

public static void main(String[] args)

{

double[] myList = {1.9, 2.9, 3.4, 3.5};
    for (int i = 0; i < 5; i++) {
        System.out.println(myList[i]);
    }
}

}
"""

# I can just grab the name from the Assignment column
program_name = """HelloPrinter.java"""

program_compiled_name = program_name.replace(".java", "")

text_file = open(program_name, "w")
text_file.write(loadProgram)
text_file.close()

call(["javac", program_name])
proc = subprocess.Popen(["java", program_compiled_name],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout_value, stderr_value = proc.communicate('through stdin to stdout')
#print '\tpass through:', repr(stdout_value)
print 'stderr:', repr(stderr_value)

call(["rm", program_name])
call(["rm", program_compiled_name + ".class"])
