"""#

This module contains functions for analyzing a grammar, finding its
NULLABLE, FIRST, FOLLOW and SELECT sets, and determining if it is LL(1).

A grammar is represented as a list of rules of the form (head, body)
where head is the goal non-terminal, and body is a tuple of symbols,
or the empty tuple () for an epsilon rule.

"""

from symbols import *


grammar_recitation = [
    (P, (S, EOF)),                     # P -> S EOF
    (S, (ID, ASSIGN, E)),              # S -> id := E
    (S, (IF, LP, E, RP, S, ELSE, S)),  # S -> if (E) S else S
    (E, (T, EP)),                      # E -> T EP
    (T, (ID,)),                        # T -> id
    (T, (LP, E, RP)),                  # T -> (E)
    (EP, ()),                          # EP -> epsilon
    (EP, (PLUS, E)),                   # EP -> + E
]


def calculate_nullable(terminals, nonterminals, grammar):
    """
    Return the set of nullable nonterminals in the given grammar.

    terminals and nonterminals are sets, grammer is a list of rules as
    explained above.

    --- DO NOT MODIFY THIS FUNCTION ---
    """
    nullable = set()
    for head, body in grammar:
        if body == ():
            nullable.add(head)
    changing = True
    while changing:
        changing = False
        for head, body in grammar:
            if set(body).issubset(nullable) and head not in nullable:
                nullable.add(head)
                changing = True
    return nullable


def calculate_first(terminals, nonterminals, grammar, nullable):
    """
    Return a dictionary mapping terminals and nonterminals to their FIRST set
    """
    first = dict()
    for t in terminals:
        first[t] = set([t])
    for a in nonterminals:
        first[a] = set()
    changing = True
    while changing:
        changing = False
        for head, body in grammar:
            for i in range (0,len(body)):
            	if set(body[0:i]).issubset(nullable):
                    if not first.get(body[i]).issubset(first.get(head)):
                        first[head] = (first.get(head)).union(first.get(body[i]))
                        changing = True
    return first


def calculate_follow(terminals, nonterminals, grammar, nullable, first):
    """
    Return a dictionary mapping terminals and nonterminals to their FOLLOW set
    """
    follow = dict()
    for a in nonterminals.union(terminals):
        follow[a] = set()
    changing = True
    while changing:
        changing = False
        for head, body in grammar:
            n = len(body)
            for i in range(0, n):
                for j in range(i+1, n):
                    if i+1 == j or set(body[i+1:j]).issubset(nullable):
                        if not first[body[j]].issubset(follow[body[i]]):
                            follow[body[i]] = follow[body[i]].union(first[body[j]])
                            changing = True
                if set(body[i+1:n]).issubset(nullable):
                    if not follow[head].issubset(follow[body[i]]):
                       follow[body[i]] = follow[body[i]].union(follow[head])
                       changing = True
    return follow


def calculate_select(terminals, nonterminals, grammar, nullable, first, follow):
    """
    Return a dictionary mapping rules to their SELECT (a.k.a. PREDICT) set
    """
    select = dict()
    for rule in grammar:
		select[rule] = set()
    for rule in grammar:
		head, body = rule
		if not set(body).issubset(nullable):
			select[rule] = first[body[0]]
		else:
			select[rule] = select[rule].union(follow[head])
			if len(body) != 0:
				select[rule] = select[rule].union(first[body[0]])		
    return select


def format_rule(r):
    """
    --- DO NOT MODIFY THIS FUNCTION ---
    """
    return "{} -> {}".format(r[0], ' '.join(r[1]))


def find_terminals_and_nonterminals(grammar):
    """
    Find the terminals and nonterminals appearing in the given grammar.

    --- DO NOT MODIFY THIS FUNCTION ---
    """
    symbols = set()
    nonterminals = set()
    for head, body in grammar:
        nonterminals.add(head)
        symbols.update(body)
    terminals = symbols.difference(nonterminals)
    return terminals, nonterminals


def analyze_grammar(grammar):
    """
    Use other functions in this module to analyze the grammar and
    check if it is LL(1).

    --- DO NOT MODIFY THIS FUNCTION ---
    """
    print "Analyzing grammar:"
    for r in grammar:
        print "    " + format_rule(r)
    print

    terminals, nonterminals = find_terminals_and_nonterminals(grammar)
    print "terminals = ", terminals
    print "nonterminals = ", nonterminals
    print

    nullable = calculate_nullable(terminals, nonterminals, grammar)
    print "nullable = ", nullable
    print

    first = calculate_first(terminals, nonterminals, grammar, nullable)
    for k in sorted(first.keys()):
        print "first({}) = {}".format(k, first[k])
    print

    follow = calculate_follow(terminals, nonterminals, grammar, nullable, first)
    for k in sorted(follow.keys()):
        print "follow({}) = {}".format(k, follow[k])
    print

    select = calculate_select(terminals, nonterminals, grammar, nullable, first, follow)
    for k in sorted(select.keys()):
        print "select({}) = {}".format(format_rule(k), select[k])
    print

    ll1 = True
    n = len(grammar)
    for i in range(n):
        for j in range(i+1, n):
            r1 = grammar[i]
            r2 = grammar[j]
            if r1[0] == r2[0] and len(select[r1].intersection(select[r2])) > 0:
                ll1 = False
                print "Grammar is not LL(1), as the following rules have intersecting SELECT sets:"
                print "    " + format_rule(r1)
                print "    " + format_rule(r2)
    if ll1:
        print "Grammar is LL(1)."
    print


grammar_json_4a = [
    (json, (obj, EOF)),                     # json-> obj EOF
    (obj, (LB, RB)),                        # obj-> {}
    (obj, (LB, members, RB)),               # obj-> {members}
    (members, (keyvalue, )),                # members-> keyvalue
    (members, (members, COMMA, members)),   # members-> members,members
    (keyvalue, (STRING, COLON, value)),     # keyvalue-> string : value
    (value, (STRING,)),			            # value -> string
    (value, (INT,)),		                # value -> int
    (value, (obj,))			                # value -> obj
]

grammar_json_4b = [
    (json, (obj, EOF)),                     # json-> obj EOF
    (obj, (LB, Y)),                         # obj-> {Y
    (Y, (RB)),                              # Y-> }
    (Y, (members, RB)),                     # Y-> members}
    (members, (keyvalue, X)),               # members-> keyvalue X
    (X, ()),                                # X-> epsilon
    (X, (COMMA, members)),                  # X-> , members
    (keyvalue, (STRING, COLON, value)),     # keyvalue-> string : value
    (value, (STRING,)),                     # value -> string
    (value, (INT,)),                        # value -> int
    (value, (obj,))                         # value -> obj
]

grammar_json_4c = [
    (json, (obj, EOF)),                     # json-> obj EOF
    (obj, (LB, first_member, RB)),          # obj-> {first_member}
    (first_member, ()),                     # first_member-> epsilon
    (first_member, (members,)),             # first_member-> members
    (members, (keyvalue, X)),               # members-> keyvalue X
    (X, (COMMA, members)),                  # X-> , members X
    (X, ()),                                # X-> epsilon
    (keyvalue, (STRING, COLON, value)),     # keyvalue-> string : value
    (value, (STRING,)),                     # value -> string
    (value, (INT,)),                        # value -> int
    (value, (obj,))                         # value -> obj
]

grammar_json_6 = [
    (json, (obj, EOF)),                     # json-> obj EOF
    (obj, (LB, first_member, RB)),          # obj-> {first_member}
    (first_member, ()),                     # first_member-> epsilon
    (first_member, (members,)),              # first_member-> members
    (members, (keyvalue, X)),               # members-> keyvalue X
    (X, (COMMA, members)),                  # X-> , members X
    (X, ()),                                # X-> epsilon
    (keyvalue, (STRING, COLON, value)),     # keyvalue-> string : value
    (value, (STRING,)),                     # value -> string
    (value, (INT,)),                        # value -> int
    (value, (obj,)),                        # value -> obj
    (value, (array,)),                      # value -> array
    (array, (LP, first ,RP)),               # array -> [first]
    (first, ()),                            # first -> epsilon
    (first, (array_vals,)),                 # first -> array_vals
    (array_vals, (value, Y)),               # arrat_vals -> value Y
    (Y, ()),                                # Y -> epsilon
    (Y, (COMMA, array_vals))                # Y -> , array_vals
]



def main():
    analyze_grammar(grammar_recitation)
    print
    analyze_grammar(grammar_json_4a)
    print
    analyze_grammar(grammar_json_4b)
    print
    analyze_grammar(grammar_json_4c)
    print
    analyze_grammar(grammar_json_6)
    print

    #
    # --- ADD MORE TEST CASES HERE ---
    #


if __name__ == '__main__':
    main()
