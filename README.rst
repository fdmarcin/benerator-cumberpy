==================
Benerator Cumberpy
==================

Benerator Cumberpy is a name generator written in Python, that generates word pairs similar to "Benedict Cumberbatch". There already exist generators like this. However, they create new words, such as "Boobiedook Cumberfinkle".

Benerator Cumberpy will create pairs of existing English words that fullfil certain criteria. Examples could include "Benefits Coordination" or "Benevolent Cucumber". There are over 480 million possible combinations.

The script works both in Python 2 and 3.

**********************************
Install and run Benerator Cumberpy
**********************************

0. Install Python, and create a virtualenv.
1. Clone or download this repo.
2. ``cd`` into the project folder and install with ``pip install -e .`` (note the full stop at the end). If you're using a virtualenv, you may need to deactivate and activate it before the first use.
3. In your terminal, run ``hello-ben``. Your console will print a sentence like "Hello there, my name is Beetleweed Correctioner".

.. TO DO: Add info about importing and using in scripts

For added hilarity, pipe the output of **ben-hello** through ``cowsay`` (`cowsay for windows <https://github.com/kanej/Posh-Cowsay/>`_, Linux – ``apt install cowsay`` or whatever else your distro uses). Make sure to check the alternative "cows" – try running ``hello-ben | cowsay -f stegosaurus``.

****************************
How Benerator Cumberpy works
****************************

I found a list of English words to use. I used `this one <https://github.com/dwyl/english-words>`_. Then I made two lists – ``first_names.txt`` and ``last_names.txt`` based on the following criteria:

First name (end result: 16692 words):
* starts with "B"
* is at least 6 letters long
* is not Benedict

Last name (end result: 28786 words):
* starts with "C" or "K"
* is at least 6 letters long
* does not start with "ch"
* is not Cumberbatch, though it wasn't in the dataset anyway
