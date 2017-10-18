==================
Benerator Cumberpy
==================

Benerator Cumberpy is a name generator written in Python, that generates word pairs similar to "Benedict Cumberbatch". There already exist generators like this. However, they create new words, such as "Boobiedook Cumberfinkle".

Benerator Cumberpy will create pairs of existing English words that fullfil certain criteria. Examples could include "Benefits Coordination" or "Benevolent Cucumber". There are over 480 million possible combinations.

The script works both in Python 2 and 3.

**********************************
Install and run Benerator Cumberpy
**********************************

Make sure you have Python installed, and (optionally) create a virtualenv.

To install Benerator Cumberpy run ``pip install benedict_cumberpy``

To run Benedict Cumberpy open up your terminal and run ``hello-ben``. Your console will print a sentence like "Hello there, my name is Bronzelike Certificate.".

For added hilarity, pipe the output of **hello-ben** through ``cowsay`` ( Win: `cowsay for windows <https://github.com/kanej/Posh-Cowsay/>`_, Linux: ``apt install cowsay`` or whatever else your distro uses, OSX: if you have HomeBrew installed – ``brew install cowsay``).

Example:

.. code-block::

  $ hello-ben | cowsay -f stegosaurus
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

You can also use Benerator Cumberpy in your python script. The ``benerate_name`` function will return only the name+surname pair.

For example:

.. code-block:: python

  # your_script.py
  from benerator_cumberpy import hello
  from benerator_cumberpy import benerate_name
 
  print("You know who you can always count on? " + str(benerate_name()) + "!")
  hello()

.. code-block::

  $ python your_script.py
  You know who you can always count on? Bestselling Corridors!
  Hello there, my name is Belial Cobalt.


*****************************
Where do the words come from?
*****************************

I found a list of English words to use – `this one <https://github.com/dwyl/english-words>`_. Then I made two lists – ``first_names.txt`` and ``last_names.txt`` based on the following criteria:

First name (end result: 16692 words):

* starts with "B"
* is at least 6 letters long
* is not Benedict

Last name (end result: 28786 words):

* starts with "C" or "K"
* is at least 6 letters long
* does not start with "ch"
* is not Cumberbatch, though it wasn't in the dataset anyway
