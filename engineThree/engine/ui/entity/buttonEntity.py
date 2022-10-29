from ui.action import *

# make color an init value
class buttonEntity(object):
    def __init__(self, dimensions = (0,0,10,20), color = (255,255,100)):
        self.dimensions = dimensions
        self.actions = []
        self.color = color
        self.entity_state = None
        self.name = "button_entity"
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

    def is_inside(self, pos):
        if pos[0] < self.dimensions[0]:
            return False
        if pos[0] > self.dimensions[0] + self.dimensions[2]:
            return False
        if pos[1] < self.dimensions[1]:
            return False
        if pos[1] > self.dimensions[3] + self.dimensions[1]:
            return False
        return True