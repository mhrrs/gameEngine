from pygame.locals import *
import pygame

class decrementCountdownAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.children = []
        self.name = "decrement_countdown_timer"
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        if self.entity_state.active == False:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.decrementCountdown(data)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def decrementCountdown(self,data):
        for i in self.entity_state.actions:
            if i.name == "start_timer":
                timer = i
            if i.name == "alarm_timer":
                alarm = i

        if self.entity_state.elapsed_time > alarm.countdown:
            if alarm.countdown > 500:
                alarm.countdown -= 250
            timer.active = False
            print("new countdown: ", alarm.countdown)

        if timer.active == True:
            if alarm.countdown > 500:
                alarm.countdown -= 250
            timer.active = False
            print("new countdown: ", alarm.countdown)