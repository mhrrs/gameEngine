from pygame.locals import *
import pygame

class timerEntity(object):
    def __init__(self):
        self.actions = []
        self.entity_state = None
        self.name = "timer_entity"
        self.verbose = False
        self.active = True
        self.current_time = 0
        self.clock = pygame.time.Clock()
        self.elapsed_time = 0
        self.start_time = 0
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

    def get_start_time(self):
       self.start_time = 0
       return self.start_time

    def tick(self):
       self.current_time += self.clock.tick(45)
       return self.current_time

    def get_elapsed_time(self):
       self.elapsed_time = abs(self.current_time - self.start_time)
       return self.elapsed_time