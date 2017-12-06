from file_parser import SymbolCleaner
terminal_list = [
        "program",
        ";",
        "var",
        "begin",
        "end.",
        ":",
        ",",
        "integer",
        "print(",
        ");",
        "=",
        "+",
        "-",
        "/",
        "*",
        "(",
        ")",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "p",
        "q",
        "r",
        "s",
        "$"
    ]

non_terminals = [
        "prog",
        "id-after",
        "type",
        "write",
        "expr-prime",
        "term-prime",
        "factor",
        "number-after",
        "sign",
        "digit",
        "letter",
        "id",
        "stat",
        "number",
        "dec",
        "assign",
        "dec-list",
        "dec-prime",
        "stat-list",
        "stat-list-prime",
        "term",
        "expr"
    ]

# Make the table
table = {}
for non_terminal in non_terminals:
    non_terminal_terminals = {}
    for terminal in terminal_list:
        non_terminal_terminals[terminal] = "!"
    table[non_terminal] = non_terminal_terminals

def add_to_table(key, list_of_intersections, value):
    for intersection in list_of_intersections:
        table[key][intersection] = value

# Prog
add_to_table('prog', ['program'], "program id ; var dec-list begin stat-list end.")
add_to_table('prog', ['$'], "program id ; var dec-list begin stat-list end.")

# ID
add_to_table('id', ['p', 'q', 'r', 's'], "letter id-after")

# ID-After
add_to_table('id-after', ['p', 'q', 'r', 's'], "letter id-after")
add_to_table('id-after', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "digit id-after")
add_to_table('id-after', ['=', ');', ',', ';', '*', '/', ':', '+', '-', ')'], "")

# Dec-List
add_to_table('dec-list', ['p', 'q', 'r', 's'], "dec : type ;")

# Dec
add_to_table('dec', ['p', 'q', 'r', 's'], "id , dec-prime")

# Dec-Prime
add_to_table('dec-prime', ['p', 'q', 'r', 's'], "id , dec-prime")
add_to_table('dec-prime', [':'], "")

# Type
add_to_table('type', ['integer'], "integer")

# Stat-List
add_to_table('stat-list', ['print(', 'p', 'q', 'r', 's'], "stat stat-list-prime")

# Stat-List Prime
add_to_table('stat-list-prime', ['print(', 'p', 'q', 'r', 's'], "stat stat-list-prime")
add_to_table('stat-list-prime', ['end.'], "")

# Stat
table['stat']['print('] = "write"
table['stat']['p'] = table['stat']['q'] = table['stat']['r'] = table['stat']['s'] = "assign"

# Write
table['write']['print('] = "print( id );"

# Assign
add_to_table('assign', ['p', 'q', 'r', 's'], "id = expr")

# Expr
add_to_table('expr', ['(', 'p', 'q', 'r', 's', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "term expr-prime")

# Expr-Prime
add_to_table('expr-prime', ['+'], "+ term expr-prime")
add_to_table('expr-prime', ['-'], "- term expr-prime")
add_to_table('expr-prime', [')', ';'], "")

# Term
add_to_table('term', ['(', 'p', 'q', 'r', 's', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "factor term-prime")

# Term-Prime
add_to_table('term-prime', ['*'], "* term term-prime")
add_to_table('term-prime', ['/'], "/ term term-prime")
add_to_table('term-prime', ['+', '-', ')', ';'], "")

# Factor
add_to_table('factor', ['p', 'q', 'r', 's'], "id")
add_to_table('factor', ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "number")
add_to_table('factor', ['('], "( expr )")

# Number
add_to_table('number', ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "sign digit number-after")

# Number-After
add_to_table('number-after', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "digit")
add_to_table('term-prime', ['+', '-', '*', '/', ')', ';'], "")

# Sign
add_to_table('sign', ['+'], "+")
add_to_table('sign', ['-'], "-")
add_to_table('sign', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "")

# Digit
add_to_table('digit', ['0'], '0')
add_to_table('digit', ['1'], '1')
add_to_table('digit', ['2'], '2')
add_to_table('digit', ['3'], '3')
add_to_table('digit', ['4'], '4')
add_to_table('digit', ['5'], '5')
add_to_table('digit', ['6'], '6')
add_to_table('digit', ['7'], '7')
add_to_table('digit', ['8'], '8')
add_to_table('digit', ['9'], '9')

# Letter
add_to_table('letter', ['p'], 'p')
add_to_table('letter', ['q'], 'q')
add_to_table('letter', ['r'], 'r')
add_to_table('letter', ['s'], 's')

for entry in table:
    output = entry + ":\n"
    for var in table[entry]:
        output += var + " " + table[entry][var] + ", "
    print(output + '\n')

cleaner = SymbolCleaner()
file = cleaner.do_file_cleanup().split(' ')

print(file)
