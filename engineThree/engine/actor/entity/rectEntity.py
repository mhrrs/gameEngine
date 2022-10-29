from actor.action import *

# make color an init value
class rectangularEntity(object):
    def __init__(self, x, y, width, height, color):
        self.dimensions = (x, y, width, height)
        self.actions = []
        self.location = (x,y)
        self.color = color
        self.entity_state = None
        self.name = "rect_entity"
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return