# Written for python 3.5.3
import random


endname = ""

# choose first name
names1 = open('first-names.txt').read().splitlines()
endname += random.choice(names1)
open('first-names.txt').close

endname += " "

# choose second name
names2 = open('last-names.txt').read().splitlines()
endname += random.choice(names2)
open('last-names.txt').close

print(endname)
