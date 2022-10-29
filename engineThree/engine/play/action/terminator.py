import pygame
from pygame.locals import *
import sys

class Terminate():
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.name = "quit_action"
        self.children = []

    def condition_to_act(self, event):
        if self.entity_state.active == False:
            return False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return True
        if event.type == QUIT:
            return True
        return False

    def act(self, event):
        if self.condition_to_act(event):
            self.entity_state.terminate()
        return