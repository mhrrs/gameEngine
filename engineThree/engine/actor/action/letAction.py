from pygame.locals import *
from actor.entity import *
import pygame


class drawLetterAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_letter_action"
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        elif self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    # ensure that this letter is active
    def act(self, event):
        if self.condition_to_act(event):
            self.draw_letter(event)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    # blit letter onto screen
    def draw_letter(self, data):
        fontObj = pygame.font.Font("freesansbold.ttf", 25)
        text_surface_object = fontObj.render(self.entity_state.letter, True, (255,255,0), (0,0,0))
        data.blit(text_surface_object,self.entity_state.location)
        return 