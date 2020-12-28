import random


def benerate_name():

    endname = ""

    # choose first name
    with open('data/first-names.txt') as f:
        data = f.read().splitlines()
        endname += random.choice(data).capitalize()

    endname += " "

    # choose second name
    with open('data/last-names.txt') as f:
        data = f.read().splitlines()
        endname += random.choice(data).capitalize()

    return endname


def hello():

    print("Hello there, my name is " + benerate_name() + ".")

if __name__ == "__main__":
    benerate_name()
