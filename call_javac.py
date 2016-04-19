import subprocess

# I can grab this from the program column!
loadProgram = """public class HelloPrinter
{

public static void main(String[] args)

{

System.out.println("Hello");//displays text

System.out.print("World");//displays text

//System.out.print("!");

}

}"""

# I can just grab the name from the Assignment column
program_name = """HelloPrinter.java"""

program_compiled_name = program_name.replace(".java", "")

text_file = open(program_name, "w")
text_file.write(loadProgram)
text_file.close()

call(["javac", program_name])

process = subprocess.Popen(["java", program_compiled_name], stdout=subprocess.PIPE)
out, err = process.communicate()
print(out)

call(["rm", program_name])
call(["rm", program_compiled_name + ".class"])
