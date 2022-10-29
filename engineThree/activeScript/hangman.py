import pygame, sys
from pygame.locals import *

# adding folders
sys.path.append('C://Users//Michael Harris//Desktop//Masters CS//Clemson MSCS//2D_gameEngineConstruction//hangmanProject//engineOne//engine')

import actor as ac
import play as pl
from english_words import english_words_lower_alpha_set
import random

def main():
    pygame.init()

    #generate random word
    while True:
        selectWord = random.choice(tuple(english_words_lower_alpha_set))
        if len(selectWord) > 4 and len(selectWord) < 9:
            break

    
    # create a list of letter entities to call upon later
    print(selectWord)
    x = 0
    list_o_letters = []
    list_o_rects = []
    alphabet = "abcdefghijklm"
    al = list(alphabet)
    alphabetTwo = "nopqrstuvwxyz"
    alTwo = list(alphabetTwo)

    # list for letters that display wrong letters to the screen
    x = 0
    for i in al:
        # make letter
        a_letter = str(i)
        letter = ac.make_letter((100+x), 100, a_letter)
        letter.active = False
        letter.insert_action(ac.make_draw_letter())
        letter.name = str(i)+"_al_letter"
        list_o_letters.append(letter)
        x += 20

    # list for letters that display second half of wrong letters to the screen
    x = 0
    for i in alTwo:
        # make letter
        a_letter = str(i)
        letter = ac.make_letter((100+x), 200, a_letter)
        letter.active = False
        letter.insert_action(ac.make_draw_letter())
        letter.name = str(i)+"_al_letter"
        list_o_letters.append(letter)
        x += 20

    x = 0
    # list of letters and rects to be used in the word-to-guess location
    for i in selectWord:
        # make letter
        a_letter = str(i)
        letter = ac.make_letter((100+x), 600, a_letter)
        letter.active = False
        letter.insert_action(ac.make_draw_letter())
        letter.name = str(i)+"_letter"
        list_o_letters.append(letter)
        
        # make rect
        rect = ac.make_basic_rectangle((100+x), 600, 40, 40, (0,255,0))
        rect.active = True
        rect.insert_action(ac.make_draw_rectangle())
        rect.name = str(i)+"_rect"
        list_o_rects.append(rect)
        x+=100

    # render letters for failed game state
    x = 0
    for i in "failed game.":
        a_letter = str(i)
        letter = ac.make_letter((100+x), 600, a_letter)
        letter.active = False
        letter.insert_action(ac.make_draw_letter())
        letter.name = str(i)+"_endGame"
        list_o_letters.append(letter)
        x+=75

    # render letters for success game state
    x = 0
    for i in "You win!":
        a_letter = str(i)
        letter = ac.make_letter((350+x), 600, a_letter)
        letter.active = False
        letter.insert_action(ac.make_draw_letter())
        letter.name = str(i)+"_winGame"
        list_o_letters.append(letter)
        x+=50

    # make hangman entity and pass it the info regarding the get_guess_letter action class
    logic_center = ac.get_guess_letter(selectWord)
    hman = ac.make_man_entity()
    hman.insert_action(ac.make_man_action())
    hman.insert_action(logic_center)
    hman.name = "hanging_man"

    # display window
    viewer = pl.frameViewerEntity()
    viewer.insert_action(pl.make_terminate_action())
    window = pl.make_frameViewerAction()

    # add game logic into frame viewer entity
    viewer.insert_action(logic_center)

    # insert hanger in frame viewer action-> draws hanger
    hanger = ac.make_hanger_entity()
    hanger.insert_action(ac.make_hanger_action())
    hanger.name = "hanger object"
    window.insert_entity(hanger)

    # insert man in frame viewer action-> draws man
    window.insert_entity(hman)

    # inserting window into entity
    viewer.insert_action(window)

    game_content = [viewer]
    
    # adding letters and rectangles to necessary action/entity class
    for i in list_o_letters:
        window.insert_entity(i)
        game_content.append(i)
    
    for i in list_o_rects:
        window.insert_entity(i)
        game_content.append(i)

    # run game loop
    game = pl.make_gameLoopAction(game_content)
    game.loop()


main()
