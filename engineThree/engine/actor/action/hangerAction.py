import actor as ac
import pygame
from pygame.locals import *


class drawHangerAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.entity = None
        self.verbose = False
        self.name = "draw_hanger_action"
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        elif self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.create_hanger(data)

        if self.verbose:
            print(self.name, " for ", self.entity_state.name)
        return


    # create rectangles and draw them on start of the game
    def create_hanger(self, data):
        rect = ac.make_basic_rectangle(250, 500, 400, 20, (255,0,0))
        rect.active = True
        rect.insert_action(ac.make_draw_rectangle())
        rect.name = "hanger1"
        pygame.draw.rect(data,rect.color,rect.dimensions)

        rect = ac.make_basic_rectangle(400, 100, 30, 400, (255,0,0))
        rect.active = True
        rect.insert_action(ac.make_draw_rectangle())
        rect.name = "hanger2"
        pygame.draw.rect(data,rect.color,rect.dimensions)

        rect = ac.make_basic_rectangle(400, 100, 300, 20, (255,0,0))
        rect.active = True
        rect.insert_action(ac.make_draw_rectangle())
        rect.name = "hanger3"
        pygame.draw.rect(data,rect.color,rect.dimensions)

        rect = ac.make_basic_rectangle(685, 100, 30, 100, (255,0,0))
        rect.active = True
        rect.insert_action(ac.make_draw_rectangle())
        rect.name = "hanger4"
        pygame.draw.rect(data,rect.color,rect.dimensions)