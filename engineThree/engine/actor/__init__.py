from pygame.locals import *
from actor.entity.rectEntity import *
from actor.action.rectAction import *
from actor.entity.circEntity import *
from actor.action.circAction import *
from actor.entity.letEntity import *
from actor.action.letAction import *
from actor.action.gLetterAction import *
from actor.entity.hangEntity import *
from actor.action.hangerAction import *
from actor.action.hmanAction import *
from actor.entity.hmanEntity import *

# make rect functions
def make_basic_rectangle(x, y, width, height, color):
    result = rectangularEntity(x, y, width, height, color)
    return result

def make_draw_rectangle():
    return drawRectangleAction()

# make circle functions
def make_basic_circle(x, y, radius):
    result = circleEntity(x, y, radius)
    return result

def make_draw_circle():
    result =  drawCircleAction()
    return result

# make letter functions
def make_letter(x,y,word):
    result = letterEntity(x,y,word)
    return result

def make_draw_letter():
    return drawLetterAction()

# take letter inputs
def get_guess_letter(word):
    result = guessLetterAction(word)
    return result

def make_hanger_entity():
    return hangerEntity()

def make_hanger_action():
    return drawHangerAction()

def make_man_entity():
    return manEntity()

def make_man_action():
    return manAction()