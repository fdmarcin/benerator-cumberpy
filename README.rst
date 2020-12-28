==================
Benerator Cumberpy
==================

Benerator Cumberpy is a name generator written in Python that generates word pairs similar to "Benedict Cumberbatch". There already exist generators like this. However, they create new words, such as "Boobiedook Cumberfinkle".

Benerator Cumberpy will create pairs of existing English words that fullfil certain criteria. Examples could include "Benefits Coordination" or "Benevolent Cucumber". There are over 480 million possible combinations.

The script works both in Python 2 and 3.

**********************************
Install and run Benerator Cumberpy
**********************************

Make sure you have Python installed, and (optionally) create a virtualenv.

To install Benerator Cumberpy, run ``pip install benerator-cumberpy``

To run Benedict Cumberpy in terminal, run:

.. list-table:: Available commands
    :header-rows: 1

    * - Command
      - Description
    * - ``benerate``
      - Print only a name-surname pair.
    * - ``hello-ben``
      - Print a sentence like "Hello there, my name is Bronzelike Certificate.".

For added hilarity, pipe the output of ``hello-ben`` through ``cowsay`` (Win: `cowsay for Windows <https://github.com/kanej/Posh-Cowsay/>`_, Linux: ``apt install cowsay`` or whatever else your distro uses, OSX: if you have HomeBrew installed – ``brew install cowsay``).

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

You can also use Benerator Cumberpy in your Python script.

For example:

.. code-block:: python

  # your_script.py
  from benerator_cumberpy import benerate_name
  from benerator_cumberpy import hello

  benerate_name()
  hello()

.. code-block::

  $ python your_script.py

  Bestselling Corridors
  Hello there, my name is Belial Cobalt.


*****************************
Where do the words come from?
*****************************

I found a list of English words to use – `this one <https://github.com/dwyl/english-words>`_.
Then I made two lists – ``first_names.txt`` and ``last_names.txt`` based on the following criteria:

First name (end result: 16692 words):

* starts with "B"
* is at least 6 letters long
* is not Benedict

Last name (end result: 28786 words):

* starts with "C" or "K"
* is at least 6 letters long
* does not start with "ch"
* is not Cumberbatch, though it wasn't in the dataset anyway
