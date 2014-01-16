Logic Formatter
=========

Simple program I wrote for easily converting make-shift logical connective 
symbols into the actual unicode character that they represent. Also ensures
that binary connectives are surrounded by a space. Useful for quickly jotting 
notes and later running the program on the file to improve readability.


|Connective  | Before | After |
| ---------- |-------:| -----:|
|Negation    | ~      | ¬     |
|Conjuction  | /\     | ∧     |
|Disjunction | \/     | ∨     |
|Exclusive or| <>     | ⊕     |
|Implies     | =>     | →     |
|Equivalence | ==     | ≡     |

Usage
------
Add the file to be formatted as a command-line argument after python file.

`LogicFormatter.py filename`

Requires Python 3.