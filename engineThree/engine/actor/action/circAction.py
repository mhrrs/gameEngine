from pygame.locals import *
from actor.entity import *
import pygame



class drawCircleAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_circle_action"
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
            self.draw_circle(event)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def draw_circle(self, data):
        return pygame.draw.circle(data, self.entity_state.color, self.entity_state.dimensions, self.entity_state.radius, 0)