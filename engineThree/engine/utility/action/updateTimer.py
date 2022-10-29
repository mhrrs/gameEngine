from pygame.locals import *
import pygame

class updateTimerAction(object):
    def __init__(self):
        self.types = ["loop"]
        self.entity_state = None
        self.verbose = False
        self.children = []
        self.name = "update_timer"
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.update_timer(data)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def update_timer(self,data):
        self.entity_state.tick()
        passed_time = self.entity_state.get_elapsed_time()

        # find alarm entity in entity_state actions
        for i in self.entity_state.actions:
            if i.name == "alarm_timer":
                countdown_clock = i.countdown

        # if timer expires, activate start_timer, and sound and then call alarm
        if passed_time > countdown_clock:
            for i in self.children:
                i.active = True
                i.act(data)
                i.active = False

        print("passed time: ", passed_time)