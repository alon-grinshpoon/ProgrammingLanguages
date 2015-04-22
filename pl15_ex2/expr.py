"""

Semantics of arithmetic and boolean expressions.

Implemented according to
http://www.daimi.au.dk/~bra8130/Wiley_book/wiley.pdf (the book).

"""

from while_ast import *


tt = 'tt'
ff = 'ff'


def eval_arith_expr(e, s):
    """
    Semantics of arithmetic expressions.

    Implements Table 1.1 from the book.

    --- MODIFY THIS FUNCTION IN QUESTION 1 ---

    """

    if type(e) is ALit:
        return e.value

    elif type(e) is Var:
        return s[e.var_name]

    elif type(e) is Plus:
        return eval_arith_expr(e.a1, s) + eval_arith_expr(e.a2, s)

    elif type(e) is Times:
        return eval_arith_expr(e.a1, s) * eval_arith_expr(e.a2, s)

    elif type(e) is Minus:
        return eval_arith_expr(e.a1, s) - eval_arith_expr(e.a2, s)

    elif type(e) is Div:
        return eval_arith_expr(e.a1, s) / eval_arith_expr(e.a2, s)

    elif type(e) is Mod:
        return eval_arith_expr(e.a1, s) % eval_arith_expr(e.a2, s)

    else:
        assert False # Error


def eval_bool_expr(e, s):
    """
    Semantics of arithmetic expressions

    Implements Table 1.2 from the book.

    --- MODIFY THIS FUNCTION IN QUESTION 1 ---

    """

    if type(e) is BLit:
        return e.value

    elif type(e) is Eq:
        if eval_arith_expr(e.a1, s) == eval_arith_expr(e.a2, s):
            return tt
        return ff

    elif type(e) is LE:
        if eval_arith_expr(e.a1, s) <= eval_arith_expr(e.a2, s):
            return tt
        return ff


    elif type(e) is Not:
        if not eval_bool_expr(e.b, s) == tt:
            return tt
        return ff

    elif type(e) is And:
        if eval_bool_expr(e.b1, s) == tt and eval_bool_expr(e.b2, s) == tt:
            return tt
        return ff

    elif type(e) is Or:
        if eval_bool_expr(e.b1, s) == tt or eval_bool_expr(e.b2, s) == tt:
            return tt
        return ff

    else:
        assert False # Error


def main():
    # (x + 1) * (x - 1)
    a = Times(Plus(Var('x'), ALit(1)), Minus(Var('x'), ALit(1)))

    print a
    print eval_arith_expr(a, {'x':10})
    print

    b = And(LE(ALit(1), ALit(2)),
            Not(BLit(ff)))

    print b
    print eval_bool_expr(b, {'x':10})
    print

    #
    # --- ADD MORE TESTS HERE ---
    #

if __name__ == '__main__':
    main()