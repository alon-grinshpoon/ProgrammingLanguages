
from symbols import *

a= [1,2,3]
x= len(a)-1
print a[x]

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
            n = len(body)
            for i in range(0, n):
                print head
                print set(body[i+1:n+1])
                print set(body[i:i+1])
                print '****************************'