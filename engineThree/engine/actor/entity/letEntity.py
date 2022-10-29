from actor.action import *

class letterEntity(object):
    def __init__(self, x, y, letter):
        self.letter = letter
        self.location = (x,y)
        self.actions = []
        self.color = (255,255,255)
        self.entity_state = None
        self.name = "letter_entity"
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return