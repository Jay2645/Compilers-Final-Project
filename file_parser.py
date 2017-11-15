import re

RESERVED_WORDS = [
    'program',
    'var',
    'integer',
    'begin',
    'print',
    'end.'
]
END_OF_LINE = 0
COMMENT = 1
ASSIGNMENT = 2
INDEX = 3
VAR = 1
BEGIN = 3
END = 5

SPECIAL_SYMBOLS = [
    ';', # End of line
    '//', # Comment
    '=', # Assignment
    ',', # Index
    ':',
    '*',
    '-',
    '(',
    ')',
    '+',
]

# This function formats the lines, stripping whitespace and comments
def clean_up_lines(lines):
    statement = ''
    # Remove comments
    for line in lines:
        statement += line.split(SPECIAL_SYMBOLS[COMMENT])[0]
    
    # Strip all spaces
    statement = "".join(statement.split())

    # Remove block comments using a regular expression
    statement = re.sub('\/\*(.*?)\*\/', '', statement)

    # Separate on semicolons
    statement = re.sub(SPECIAL_SYMBOLS[END_OF_LINE], SPECIAL_SYMBOLS[END_OF_LINE] + '\n', statement)
    # Separate on var blocks
    statement = re.sub(RESERVED_WORDS[VAR], RESERVED_WORDS[VAR] + '\n', statement)
    # Separate on begin blocks
    statement = re.sub(RESERVED_WORDS[BEGIN], RESERVED_WORDS[BEGIN] + '\n', statement)
    # Separate on end blocks
    statement = re.sub(RESERVED_WORDS[END], RESERVED_WORDS[END] + '\n', statement)    
    return statement.split('\n')

# Read all line statements from a file
# Outputs a list of all found statements
def read_line_statements(line):
    current_input = ''
    line_statements = []
    for character in line:
        current_input += character
        if character in SPECIAL_SYMBOLS:
            line_statements.append(current_input[:-1])
            line_statements.append(character)
            current_input = ''
            continue
        elif current_input in RESERVED_WORDS:
            line_statements.append(current_input)
            current_input = ''
    return line_statements

# Program flow
# Open file
file = open('data.txt', 'r')

# Format file
statements = clean_up_lines(file.readlines())

# Read statements
statement_output = []
for line in statements:
    statement_output.append(read_line_statements(line))

# Write file
output_string = ''
for line in statement_output:
    for value in line:
        output_string += value + ' '
    output_string += '\n'
output_string = re.sub('  ', ' ', output_string)
print(output_string)
file = open('newdata.txt', 'w')
file.write(output_string)
