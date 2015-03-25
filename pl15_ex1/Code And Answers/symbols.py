"""
This module just contains the definitions of the terminals (tokens) and nonterminals.
"""

# terminals for JSON
LB = 'LB'          # {
RB = 'RB'          # }
LS = 'LS'          # [
RS = 'RS'          # ]
COMMA = 'COMMA'    # ,
COLON = 'COLON'    # :
INT = 'INT'        # an integer value
STRING = 'STRING'  # a string value
EOF = 'EOF'        # end of file marker

# nonterminals for JSON
json = 'json'
obj = 'obj'
members = 'members'
first_member = 'first_member'
keyvalue = 'keyvalue'
value = 'value'
X = 'X'
member = 'members'
array = 'array'

# terminals for the grammar from the recitation
LP = 'LP'          # (
RP = 'RP'          # )
ASSIGN = 'ASSIGN'  # :=
PLUS = 'PLUS'      # +
IF = 'IF'          # if
ELSE = 'ELSE'      # else
ID = 'ID'          # identifier 

# nonterminals for the grammar from the recitation
P = 'P'
S = 'S'
E = 'E'
T = 'T'
EP = 'EP'
