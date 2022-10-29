from play.action.frameViewer import *
from play.action.gameLoop import *
from play.action.terminator import *
from play.entity.frameViewerE import *
from play.entity.gameLoopE import *

# return window to be used for the rest of game
def make_frameViewerAction():
    window = frameViewerAction()
    window.entity_state = "display"
    return window

def make_frameViewerEntity(width, height):
    return frameViewerEntity((width,height))

def make_terminate_action():
    return Terminate()

# return gameLoopAction class with info already inside it's children list
def make_gameLoopAction(game_content):
    game = gameLoopAction()
    for e in game_content:
        game.insert_entity(e)
    return game