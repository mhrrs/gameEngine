from pygame.locals import *
import pygame
import random

class pressedButtonAction():
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "button_pressed_action"
        self.children = []
        self.verbose = False
        return

    def insert_children(self, a):
        self.children.append(a)
        return

    def condition_to_act(self, event):
        if self.entity_state == False:
            return False
        elif self.entity_state.active == False:
            return False
        if event.type == MOUSEBUTTONDOWN:
            pos = event.pos
            return self.entity_state.is_inside(pos)
        return False

    def act(self, event):
        if self.condition_to_act(event):
            for i in self.children:
                i.active = True
                i.act(event)
                if i.name != "start_timer":
                    i.active = False
            
            if self.verbose:
                print(self.name, " for ", self.entity_state.name + " at " + str(event.pos))
        return

