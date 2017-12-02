from file_parser import SymbolCleaner

# <prog>        -> program <id>; var <dec-list> begin <stat-list> end.
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

class State:
    def __init__(self, allowed_inputs, return_type):
        self.allowed_inputs = allowed_inputs
        self.return_type = return_type

digit_state = State([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], True)

#cleaner = SymbolCleaner()
#cleaner.do_file_cleanup()
