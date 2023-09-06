import stdio
import sys

stdio.write(sys.argv)

stdio.writeln(min(sys.argv))
sys.argv.pop(min(sys.argv))

stdio.writeln(min(sys.argv))
stdio.writeln(max(sys.argv))

