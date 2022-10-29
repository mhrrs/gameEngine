from actor.action import *

class circleEntity(object):
    def __init__(self, xcenter, ycenter, radius):
        self.dimensions = (xcenter,ycenter)
        self.radius = radius
        self.actions = []
        self.color = (0,0,255)
        self.entity_state = None
        self.name = "rect_entity"
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return