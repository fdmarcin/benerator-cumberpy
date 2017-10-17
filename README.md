## Benerator Cumberpy

Benerator Cumberpy is a name generator written in Python, that generates word pairs similar to "Benedict Cumberbatch". There already exist generators like this. However, they create new words, such as "Boobiedook Cumberfinkle".

Benerator Cumberpy will create pairs of existing English words that fullfil certain criteria. Examples could include "Benefits Coordination" or "Benevolent Cucumber".

### Running Benerator Cumberpy

0. Have python installed.
1. Clone the repo or download as zip.
2. `cd` into the folder.
3. Run `python benerator-cumber.py`

For added hilarity, pipe the output of benerator-cumber.py through `cowsay` ([cowsay for windows](https://github.com/kanej/Posh-Cowsay), Linux – `apt install cowsay` or whatever else your distro uses).

Example:

```
$ python benerator-cumber.py | cowsay -f stegosaurus
 ____________________________________
/ Hello there, my name is Beetleweed \
\ Correctioner.                      /
 ------------------------------------
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
```

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

TO DO: Figure out how to put it on a website for people who don't use the command line. Maybe github.io + [Brython](http://www.brython.info/)?.
