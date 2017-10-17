# Written for python 3.5

import random


endname = ""

# choose first name
with open('first-names.txt') as f:
    data = f.read().splitlines()
    endname += random.choice(data).capitalize()

endname += " "

# choose second name
with open('last-names.txt') as f:
    data = f.read().splitlines()
    endname += random.choice(data).capitalize()

print("Hello there, my name is " + endname + ".")
