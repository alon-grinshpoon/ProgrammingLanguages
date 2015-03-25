"""
This file contains the JSON parser.
"""

from symbols import *


class SyntaxError(Exception):
    pass


class JsonParser(object):
    def __init__(self, tokens):
        """
        Initialize the parser.
        tokens is a list of pairs of the form:
        [(t1, v1), (t2, v2), ...]
        where ti's are in terminals, and vi's are values attached to them.
        The list is in the format returned by the lexer.

        --- DO NOT MODIFY THIS FUNCTION ---

        """
        self.tokens = tokens
        self.pos = -1
        self.advance() # updates self.t, which keeps the current terminal

    def advance(self):
        """
        Return the value attached to current token, and advance by one.
        Return EOF once all tokens are exhausted.

        --- DO NOT MODIFY THIS FUNCTION ---
        
        """
        if self.pos < len(self.tokens):
            value = self.tokens[self.pos][1]
        else:
            value = EOF
        self.pos += 1
        if self.pos < len(self.tokens):
            self.t = self.tokens[self.pos][0]
        else:
            self.t = EOF
        return value

    def match(self, terminal):
        """
        Match the next token against the given terminal. Raise a
        SyntaxError if they do not match.
        If they do, return the value attached to the current token.

        --- DO NOT MODIFY THIS FUNCTION ---

        """
        if self.t == terminal:
            value = self.advance()
            print "matched {:10} {}".format(terminal, value)
            return value
        else:
            raise SyntaxError("Syntax error: expected {}, found {}".format(
                terminal, self.t))

    def parse_json(self):
        """
        --- DO NOT MODIFY THIS FUNCTION ---
        """
        if self.t in [LB]:
            c1 = self.parse_obj()
            c2 = self.match(EOF)
            return (json, (c1, c2))
        else:
            raise SyntaxError("Syntax error: no rule for token: {}".format(self.t))

    def parse_obj(self):
        if self.t in [LB]:
            lb = self.match(LB)
            first_member = self.parse_first_member()
            rb = self.match(RB)
            return (obj, (lb, first_member, rb))
        else:
            raise SyntaxError("Syntax error: no rule for token: {}".format(self.t))  
        pass    

    def parse_first_member(self):
        if self.t in [STRING]:
                members = self.parse_members()
                return (first_member, (members,))
        elif self.t in [RB]:
                return (first_member, ())
        else:
            raise SyntaxError("Syntax error: no rule for token: {}".format(self.t))

    def parse_members(self):
        if self.t in [STRING]:
            keyvalue = self.parse_keyvalue()
            X = self.parse_X();
            return (members, (keyvalue , X))
        else:
            raise SyntaxError("Syntax error: no rule for token: {}".format(self.t))     
        pass

    def parse_X(self):
        if self.t in [COMMA]:
            comma = self.match(COMMA)
            members = self.parse_members()
            return (X, (comma, members))
        elif self.t in [RB]:
            return (first_member, ())
        raise SyntaxError("Syntax error: no rule for token: {}".format(self.t))


    def parse_keyvalue(self):
        if self.t in [STRING]:
            string = self.match(STRING)
            colon = self.match(COLON)
            value = self.parse_value()
            return (keyvalue, (string, colon, value))
        else:
            raise SyntaxError("Syntax error: no rule for token: {}".format(self.t))     
        pass

    def parse_value(self):
        if self.t in [STRING]:
            string = self.match(STRING)
            return (value, (string,))
        if self.t in [INT]:
            integer = self.match(INT)
            return (value, (integer,))
        if self.t in [LB]:
            c = self.parse_obj();
            return (value, (c,))
        else:
            raise SyntaxError("Syntax error: no rule for token: {}".format(self.t))


def main():
    from lexer import lex
    from tree_to_dot import tree_to_dot

    json_example = open('json_example.json').read()
    print json_example
    tokens = lex(json_example)
    parser = JsonParser(tokens)
    parse_tree = parser.parse_json()
    dot = tree_to_dot(parse_tree)
    open('json_example.gv', 'w').write(dot)

    #
    # --- MODIFY HERE TO ADD MORE TEST CASES ---
    #



if __name__ == '__main__':
    main()
