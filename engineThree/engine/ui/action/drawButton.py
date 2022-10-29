from pygame.locals import *
import pygame

class drawRectButtonAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_button_action"
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        elif self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, event):
        if self.condition_to_act(event):
            self.draw_button(event)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    # simple draw rect function
    def draw_button(self, data):
        return pygame.draw.rect(data, self.entity_state.color, self.entity_state.dimensions)