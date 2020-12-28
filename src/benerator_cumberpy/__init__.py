import random
from pkg_resources import resource_filename


def benerate_name():

    firstnames = resource_filename(__name__, "data/first-names.txt")
    lastnames = resource_filename(__name__, "data/last-names.txt")
    endname = ""

    # choose first name
    with open(firstnames) as f:
        data = f.read().splitlines()
        endname += random.choice(data).capitalize()

    endname += " "

    # choose second name
    with open(lastnames) as f:
        data = f.read().splitlines()
        endname += random.choice(data).capitalize()

    return endname


def hello():

    print("Hello there, my name is " + benerate_name() + ".")


if __name__ == "__main__":
    benerate_name()
