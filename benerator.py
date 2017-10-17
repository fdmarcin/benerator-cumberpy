# template from http://go.chriswarrick.com/entry_points
import random

def main():

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

    print("Hello there, my name is " + main() + ".")

if __name__ == "__main__":
    main()
