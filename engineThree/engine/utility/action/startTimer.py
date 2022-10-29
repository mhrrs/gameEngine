from pygame.locals import *
import pygame

class startTimerAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "start_timer"
        self.active = False
        self.children = []
        return

    def condition_to_act(self, data):
        if self.active == False:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.start_timer(data)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def start_timer(self,data):
        # make sure time only restarts when button is pressed
        self.entity_state.get_start_time()
        self.entity_state.get_elapsed_time()
        self.entity_state.current_time = 0
        
        