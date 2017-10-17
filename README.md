## Benerator Cumberpy

Benerator Cumberpy is a name generator written in Python, that generates word pairs similar to "Benedict Cumberbatch". There already exist generators like this. However, they create new words, such as "Boobiedook Cumberfinkle".

Benerator Cumberpy will create pairs of existing English words that fullfil certain criteria. Examples could include "Benefits Coordination" or "Benevolent Cucumber".

### What I did

1. I found a list of English words to use. I used [this one](https://github.com/dwyl/english-words). I used `egrep` to select words I want.
    I made two lists – `first_names.txt` and `last_names.txt` based on certain conditions.

    First name (result: 16692 words):
    - starts with "B" (copied words beginning with B to "first-names-all.txt")
    - is at least 6 letters long (`egrep '^[a-z]{6,}$' first-names-all.txt >> first-names.txt`)
    - is not Benedict (deleted manually)

    Last name (result: 28786 words):
    - starts with "C" or "K" (copied words beginning with C or K to "first-names-all.txt")
    - is at least 6 letters long (`egrep '^[a-z]{6,}$' last-names-all.txt >> last-names.txt`)
    - does not start with "ch" (removed manually)
    - is not Cumberbatch, though it wasn't in the dataset anyway
2. I wrote the program itself.
3. I figured out how to print the name capitalized
4. TO DO: Think of implementation. GUI? Webapp?
