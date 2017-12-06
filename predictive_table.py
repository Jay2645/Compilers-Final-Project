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
table['prog']['program'] = "program id ; var dec-list begin stat-list end."
table['prog']['$'] = "program id ; var dec-list begin stat-list end."

# ID
table['id']['p'] = table['id']['q'] = table['id']['r'] = table['id']['s'] = "letter id-after"

# ID-After
table['id-after']['p'] = table['id-after']['q'] = table['id-after']['r'] = table['id-after']['s'] = "letter id-after"
table['id-after']['0'] = table['id-after']['1'] = table['id-after']['2'] = table['id-after']['3'] = \
    table['id-after']['4'] = table['id-after']['5'] = table['id-after']['6'] = table['id-after']['7'] = \
    table['id-after']['8'] = table['id-after']['9'] = "digit id-after"
table['id-after']['='] = table['id-after'][');'] = table['id-after'][','] = table['id-after'][';'] = \
    table['id-after']['*'] = table['id-after']['/'] = table['id-after'][':'] = table['id-after']['+'] = \
    table['id-after']['-'] = table['id-after'][')'] = ""

# Dec-List
table['dec-list']['p'] = table['dec-list']['q'] = table['dec-list']['r'] = table['dec-list']['s'] = "dec : type ;"

# Dec
table['dec']['p'] = table['dec']['q'] = table['dec']['r'] = table['dec']['s'] = "id , dec-prime"

# Dec-Prime
table['dec-prime']['p'] = table['dec-prime']['q'] = table['dec-prime']['r'] = table['dec-prime']['s'] = "id , dec-prime"
table['dec-prime'][':'] = ""

# Type
table['type']['integer'] = "integer"

# Stat-List
table['stat-list']['print('] = table['stat-list']['p'] = table['stat-list']['q'] = \
    table['stat-list']['r'] = table['stat-list']['s'] = "stat stat-list-prime"

# Stat-List Prime
table['stat-list-prime']['print('] = table['stat-list-prime']['p'] = table['stat-list-prime']['q'] = \
    table['stat-list-prime']['r'] = table['stat-list-prime']['s'] = "stat stat-list-prime"
table['stat-list-prime']['end.'] = ""

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

for entry in table:
    print(entry + ": " + str(table[entry]))
