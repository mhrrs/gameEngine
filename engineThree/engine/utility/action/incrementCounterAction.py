import pygame
from pygame.locals import *

class incrementAction(object):
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.children = []
        self.verbose = False
        self.name = "increment_action"
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.increment(data)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def increment(self,data):
        self.entity_state.counter += 1
        print(self.entity_state.name,": ",self.entity_state.counter)
        return