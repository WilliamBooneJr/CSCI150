import stdio
import sys

# Accept a name as a command-line argument. Write a message containing
# that name to standard output.



stdio.write('Hi, ')
stdio.writeln(str(sys.argv[-1:0:-1]))
stdio.write('How are you?')
