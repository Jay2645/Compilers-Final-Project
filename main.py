from file_parser import SymbolCleaner
from predictive_table import PredictiveInterpreter

# This runs the actual program
# First, we clean up the file
cleaner = SymbolCleaner()
# Then, we split it up into tokens
split_file = cleaner.do_file_cleanup().split(' ')

# Create our interpreter
interpreter = PredictiveInterpreter()
interpreter.make_table()
output = interpreter.try_make_stack(split_file)

# Print the results
print(output)
