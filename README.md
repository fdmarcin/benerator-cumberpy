## Benerator Cumberpy

Benerator Cumberpy is a name generator written in Python, that generates word pairs similar to "Benedict Cumberbatch". There already exist generators like this. However, they create new words, such as "Boobiedook Cumberfinkle".

Benerator Cumberpy will create pairs of existing English words that fullfil certain criteria. Examples could include "Benefits Coordination" or "Benevolent Cucumber".


TODO:
1. [X] Find a list of English words to use. For example [this one](https://github.com/dwyl/english-words). Use python or linux CLI tools to select words I want.
    I made two lists – `first_names.txt` and `last_names.txt` based on certain conditions.

    First name (result: 16692 words):
    - [X] starts with "B" (copied words beginning with B to "first-names-all.txt")
    - [X] is at least 6 letters long (`egrep '^[a-z]{6,}$' first-names-all.txt >> first-names.txt`)
    - [X] is not Benedict

    Last name (result: 33504 words):
    - [X] starts with "C" or "K" (copied words beginning with C or K to "first-names-all.txt")
    - [X] is at least 6 letters long (`egrep '^[a-z]{6,}$' last-names-all.txt >> last-names.txt`)
    - [X] is not Cumberbatch
2. [X] Write the program itself.
3. [ ] Figure out how to print the name capitalized
4. [ ] Think of implementation. GUI? Webapp?
