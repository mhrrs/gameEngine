import pygame
from pygame.locals import *
import sys

class frameViewerEntity(object):
    def __init__(self, x=400, y=300, title="untitled", name="untitled window"):
        self.types = ["display"]
        self.actions = []
        self.size = [x,y]
        self.name = name
        self.title = title
        self.verbose = False
        self.active = True
        self.window = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
        pygame.display.set_caption(title)
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return

    def setTitle(self, title):
        self.title = title
        pygame.display.set_caption(title)
        # enter verbose

    def setMode(self,sz,mode,depth):
        self.window = pygame.display.set_mode(sz, mode, depth)
        return

    # end game
    def terminate(self):
        print("Quitting game.")
        pygame.quit()
        sys.exit()
