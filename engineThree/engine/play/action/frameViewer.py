import pygame
from pygame.locals import *

class frameViewerAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.name = "frameViewerAction"
        self.verbose = False
        self.children = []
        return

    # here we are inserting actions of entity into children
    def insert_entity(self, e):
        for a in e.actions:
            if "display" in a.types:
                self.children.append(a)
        return True
    
    def condition_to_act(self, data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == False:
            return False
        return True

    # update window
    def act(self, data):
        if self.condition_to_act(data):
            self.entity_state.window.fill((0, 0, 0))
            for t in self.children:
                t.act(self.entity_state.window)
            pygame.display.flip()
        return