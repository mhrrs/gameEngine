import actor as ac
import pygame
from pygame.locals import *

class manAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_man_action"
        self.entities = []
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        elif self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.hang_him(data)

            # set .stage equal to the number of wrong guesses in "logic_center" var pumped in from main
            for i in self.entity_state.actions:
                if i.name == "active_letter_action":
                    self.entity_state.stage = len(i.wrong_guesses)
            

        if self.verbose:
            print(self.name, " for ", self.entity_state.name)
        return


    # draw hangman depending on whatever stage var is equal to 
    def hang_him(self, data):
        if self.entity_state.stage > 0:
            # head
            circ = ac.make_basic_circle(700, 200, 40)
            circ.active = True
            circ.insert_action(ac.make_draw_circle())
            circ.name = "hman_1"
            circ.actions[0].draw_circle(data)
            
        if self.entity_state.stage > 1:
            # body
            rect = ac.make_basic_rectangle(690, 235, 20, 80, (0,0,255))
            rect.active = False
            rect.insert_action(ac.make_draw_rectangle())
            rect.name = "hman_2"
            rect.actions[0].draw_rect(data)
            
        if self.entity_state.stage > 2:
            # arm 1
            rect = ac.make_basic_rectangle(690, 250, 60, 10, (0,0,255))
            rect.active = False
            rect.insert_action(ac.make_draw_rectangle())
            rect.name = "hman_3"
            rect.actions[0].draw_rect(data)

        if self.entity_state.stage > 3:
            #arm 2
            rect = ac.make_basic_rectangle(650, 250, 60, 10, (0,0,255))
            rect.active = False
            rect.insert_action(ac.make_draw_rectangle())
            rect.name = "hman_4"
            rect.actions[0].draw_rect(data)
            
        if self.entity_state.stage > 4:
            #pelvis
            rect = ac.make_basic_rectangle(670, 310, 60, 10, (0,0,255))
            rect.active = False
            rect.insert_action(ac.make_draw_rectangle())
            rect.name = "hman_5"
            rect.actions[0].draw_rect(data)
            
        if self.entity_state.stage > 5:
            #leg 1
            rect = ac.make_basic_rectangle(720, 310, 10, 60, (0,0,255))
            rect.active = False
            rect.insert_action(ac.make_draw_rectangle())
            rect.name = "hman_6"
            rect.actions[0].draw_rect(data)
            
        if self.entity_state.stage > 6:
            #leg 2
            rect = ac.make_basic_rectangle(670, 310, 10, 60, (0,0,255))
            rect.active = False
            rect.insert_action(ac.make_draw_rectangle())
            rect.name = "hman_7"
            rect.actions[0].draw_rect(data)
            