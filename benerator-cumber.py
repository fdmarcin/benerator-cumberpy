# Written for python 3.5.3

import random


endname = ""

# # using .title()
# # choose first name
# with open('first-names.txt') as f:
#     data = f.read().splitlines()
#     endname += random.choice(data)

# endname += " "

# # choose second name
# with open('last-names.txt') as f:
#     data = f.read().splitlines()
#     endname += random.choice(data)

# print("Hello there, my name is " + endname.title() + ".")

# using .capitalize()
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
