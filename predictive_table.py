class PredictiveInterpreter:
    def __init__(self):
        # This is a list of all possible terminals
        self.terminal_list = [
                "program",
                ";",
                "var",
                "begin",
                "end.",
                ":",
                ",",
                "integer",
                "print",
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

        # This is a list of all non-terminals
        self.non_terminals = [
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

        # Failure states
        # If any of these keys are encountered, we print the
        # message in the value
        self.failure_states = {
                "prog": "program is expected",
                "var": "var is expected",
                "begin": "begin is expected",
                "end.": "end. is expected",
                "type": "integer is expected"
            }

        # Make the table
        self.table = {}
        for non_terminal in self.non_terminals:
            non_terminal_terminals = {}
            for terminal in self.terminal_list:
                non_terminal_terminals[terminal] = "!"
            self.table[non_terminal] = non_terminal_terminals

    # Adds the specified key to the table
    def add_to_table(self, key, list_of_intersections, value):
        for intersection in list_of_intersections:
            self.table[key][intersection] = value

    # Creates our predictive parsing table
    def make_table(self):
        # Prog
        self.add_to_table('prog', ['program'], "program id ; var dec-list begin stat-list end.")
        self.add_to_table('prog', ['$'], "program id ; var dec-list begin stat-list end.")

        # ID
        self.add_to_table('id', ['p', 'q', 'r', 's'], "letter id-after")

        # ID-After
        self.add_to_table('id-after', ['p', 'q', 'r', 's'], "letter id-after")
        self.add_to_table('id-after', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "digit id-after")
        self.add_to_table('id-after', ['=', ')', ',', ';', '*', '/', ':', '+', '-', ')'], "")

        # Dec-List
        self.add_to_table('dec-list', ['p', 'q', 'r', 's'], "dec : type ;")

        # Dec
        self.add_to_table('dec', ['p', 'q', 'r', 's'], "id dec-prime")

        # Dec-Prime
        self.add_to_table('dec-prime', [',', 'p', 'q', 'r', 's'], ", id dec-prime")
        self.add_to_table('dec-prime', [':'], "")

        # Type
        self.add_to_table('type', ['integer'], "integer")

        # Stat-List
        self.add_to_table('stat-list', ['print', 'p', 'q', 'r', 's'], "stat stat-list-prime")

        # Stat-List Prime
        self.add_to_table('stat-list-prime', ['print', 'p', 'q', 'r', 's',], "stat stat-list-prime")
        self.add_to_table('stat-list-prime', ['end.'], "")

        # Stat
        self.add_to_table('stat', ['print'], "write")
        self.add_to_table('stat', ['p', 'q', 'r', 's'], "assign")

        # Write
        self.add_to_table('write', ['print'], "print ( id ) ;")

        # Assign
        self.add_to_table('assign', ['p', 'q', 'r', 's'], "id = expr ;")

        # Expr
        self.add_to_table('expr', ['(', 'p', 'q', 'r', 's', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "term expr-prime")

        # Expr-Prime
        self.add_to_table('expr-prime', ['+'], "+ term expr-prime")
        self.add_to_table('expr-prime', ['-'], "- term expr-prime")
        self.add_to_table('expr-prime', [')', ';'], "")

        # Term
        self.add_to_table('term', ['(', 'p', 'q', 'r', 's', '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "factor term-prime")

        # Term-Prime
        self.add_to_table('term-prime', ['*'], "* term term-prime")
        self.add_to_table('term-prime', ['/'], "/ term term-prime")
        self.add_to_table('term-prime', ['+', '-', ')', ';'], "")

        # Factor
        self.add_to_table('factor', ['p', 'q', 'r', 's'], "id")
        self.add_to_table('factor', ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "number")
        self.add_to_table('factor', ['('], "( expr )")

        # Number
        self.add_to_table('number', ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "sign digit number-after")

        # Number-After
        self.add_to_table('number-after', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "digit")
        self.add_to_table('number-after', ['+', '-', '*', '/', ')', ';'], "")

        # Sign
        self.add_to_table('sign', ['+'], "+")
        self.add_to_table('sign', ['-'], "-")
        self.add_to_table('sign', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], "")

        # Digit
        self.add_to_table('digit', ['0'], '0')
        self.add_to_table('digit', ['1'], '1')
        self.add_to_table('digit', ['2'], '2')
        self.add_to_table('digit', ['3'], '3')
        self.add_to_table('digit', ['4'], '4')
        self.add_to_table('digit', ['5'], '5')
        self.add_to_table('digit', ['6'], '6')
        self.add_to_table('digit', ['7'], '7')
        self.add_to_table('digit', ['8'], '8')
        self.add_to_table('digit', ['9'], '9')

        # Letter
        self.add_to_table('letter', ['p'], 'p')
        self.add_to_table('letter', ['q'], 'q')
        self.add_to_table('letter', ['r'], 'r')
        self.add_to_table('letter', ['s'], 's')

    # This function a read input and tries to convert
    # it to the Python equivalent
    def try_make_python_file(self, current_input):
        # Start with blank string
        output_string = ""
        
        # program becomes def
        if current_input == 'program':
            output_string += "def "
        # integer becomes 0
        elif current_input == 'integer':
            output_string += "0"
        # end, var, and begin are removed
        elif current_input == 'end.' or (
            current_input == "var") or (current_input == "begin"):
            pass
        # Colons become an equals sign
        elif current_input == ':':
            output_string += " = "
        # If we are processing a single character, then
        # we are probably in a variable name.
        # Otherwise, we are processing a reserved word.
        elif len(current_input) > 1 or (
                current_input == ',') or (
                current_input == ';'):
            output_string += current_input
            output_string += " "
        # Anything else gets processed in our postprocessing pass
        else:
            output_string += current_input
        return output_string

    # This takes a string which has been finished processing
    # and converts it to actual Python code
    def make_final_output(self, finished_string):
        # The first semicolon should become a colon,
        # followed by an indent (4 spaces)
        finished_string = finished_string.replace(';', '():\n    ', 1)
        finished_string = finished_string.replace(',', ' = 0\n    ')
        # The rest should just be the 4-space indent
        finished_string = finished_string.replace(';', '\n    ')
        return finished_string

    # This tries and processes the current stack
    def try_make_stack(self, file_input):
        current_stack = []
        current_stack.append('$')
        current_stack.append('prog')

        file_input_read = ""
        stack_input_read = ""

        output_string = ""

        # Give 500 attempts at processing the stack
        for i in range(0, 500):
            # We're done reading the file
            if file_input_read == '' and stack_input_read == '$':
                print("File compiled successfully!")
                # 
                return self.make_final_output(output_string)
            
            if file_input_read == "":
                #if current read is empty
                #reads a character/word into current_read
                file_input_read = file_input[0]
                file_input = file_input[1:]

            if stack_input_read == "":
                stack_input_read = current_stack.pop()

            if stack_input_read == '!':
                print("Error detected! Stack: " + file_input_read)
                return

            if file_input_read == stack_input_read:
                print("Matched: " + file_input_read)
                output_string += self.try_make_python_file(file_input_read)
                file_input_read = ""
                stack_input_read = ""
            else:
                try:
                    result = self.table[stack_input_read][file_input_read].split(' ')
                    for var in result[::-1]:
                        if var != '':
                            current_stack.append(var)
                    stack_input_read = ""
                except KeyError:
                    if stack_input_read in self.failure_states:
                        print(self.failure_states[stack_input_read])
                        return None
                    elif len(file_input_read) > 1:
                        temp = [x for x in file_input_read]
                        for var in temp[::-1]:
                            file_input.insert(0,var)
                        file_input_read = ""
                    elif len(file_input_read) == 1 and (
                            file_input_read not in self.terminal_list):
                        print(file_input_read,stack_input_read,sep='   ')
                        print("Error! Detected: " +
                              file_input_read + ", Expected: " + stack_input_read)
                        return None
