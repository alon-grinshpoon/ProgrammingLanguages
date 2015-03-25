
from symbols import *

grammar = [
    (P, (S, EOF)),                     # P -> S EOF
    (S, (ID, ASSIGN, E)),              # S -> id := E
    (S, (IF, LP, E, RP, S, ELSE, S)),  # S -> if (E) S else S
    (E, (T, EP)),                      # E -> T EP
    (T, (ID,)),                        # T -> id
    (T, (LP, E, RP)),                  # T -> (E)
    (EP, ()),                          # EP -> epsilon
    (EP, (PLUS, E)),                   # EP -> + E
]



for head, body in grammar:
	for i in range (0,len(body)):
		print i
		print set(body[0:i])
		print body[i]
		print '********************'