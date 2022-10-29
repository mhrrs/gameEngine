
from pygame.locals import *
import pygame

class alarmTimerAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.children = []
        self.name = "alarm_timer"
        self.countdown = 6000
        self.active = False
        return

    def insert_children(self, a):
        self.children.append(a)
        return

    def condition_to_act(self, data):
        if self.active == False:
            return False
        if self.entity_state == False:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.alarm(data)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def alarm(self,data):
        # should use the sound alarm and then also reset the timers
        for i in self.children:
            i.active = True
            i.act(data)
            i.active = False
        

        
        