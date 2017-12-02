from file_parser import SymbolCleaner

# <prog>        -> program <id> ; var <dec-list> begin <stat-list> end.
# <id>          -> <letter> {<letter> | <digit> }
# <dec-list>    -> <dec> : <type> ;
# <dec>         -> <id>, <dec> | <id>
# <type>        -> integer
# <stat-list>   -> <stat> | <stat> <stat-list>
# <stat>        -> <write> | <assign>
# <write>       -> print(<id>) ;
# <assign>      -> <id> = <expr> ;
# <expr>        -> <expr> + <term> | <expr> - <term> | <term>
# <term>        -> <term> * <factor> | <term> / <factor> | <factor>
# <factor>      -> <id> | <number> | ( <expr> )
# <number>      -> <sign> <digit>(<digit>}
# <sign>        -> +|-|lambda
# <digit>       -> 0|1|2|3|4|5|6|7|8|9
# <letter>      -> p|q|r|s

# We need to convert this to a Chomsky Type 3 grammar
# https://en.wikipedia.org/wiki/Chomsky_hierarchy#Type-3_grammars
# "Such a grammar restricts its rules to a single nonterminal on the
# left-hand side and a right-hand side consisting of a single terminal,
# possibly followed by a single nonterminal."

# After that, this answer can be used
# https://softwareengineering.stackexchange.com/a/179241

class State:
    def __init__(self, token_list):
        self.state_list = state_list
        self.value = ""
        self.entry = []
        self.output = []

    def end_of_value(self):
        self.entry.push(self.value)
        self.value = []

    def end_of_entry(self):
        self.end_of_value()
        self.output.push(self.entry)
        self.entry = []
            


digit_state = State([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], True)

#cleaner = SymbolCleaner()
#cleaner.do_file_cleanup()
