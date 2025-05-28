'''
Clue is a game 

there are 3 people 3 rooms and 3 weapons
at the start of the game we take one from each of the categories 
and put them in a envelope 
then we try to guess whats inside the envelope 
we do so by looking at some but not all of the reamaining cards

what propositional symbols are we going to need:
    mustard     ballroom    knife
    plum        kitchen     revolver
    scarlet     library     wrench

    the symbols will be true if , the symbol is inside the envelope

    using these we can create logic for the world 

    (mustard or plum or scarlet)
    (ballroom or kitchen or library)
    (knife or revolver or wrench)
        notplum
    
    notmustard or notlibrary or notrevolver
'''
import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

# Initial cards
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

# Unknown card
knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Known cards
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

check_knowledge(knowledge)