from file_parser import SymbolCleaner
terminal_list = [
        "program",
        ";",
        "var",
        "dec_list",
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
        "stat-list",
        "term",
        "expr"
    ]

# Make the table
table = {}
for non_terminal in non_terminals:
    non_terminal_terminals = {}
    for terminal in terminal_list:
        non_terminal_terminals[terminal] = "Error"
    table[non_terminal] = non_terminal_terminals

# Prog
table['prog']['program'] = "program id ; var dec_list begin stat-list end."
table['prog']['$'] = "program id ; var dec_list begin stat-list end."

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

print(table)
