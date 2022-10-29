import pygame
from pygame.locals import *

class gameLoopAction(object):
    def __init__(self):
        self.types = ["event","loop","display"]
        self.entity_state = None
        self.active = True
        self.name = "game_loop_action"
        self.verbose = False
        self.children = []
        self.event_content = []
        self.display_content = []
        self.loop_content = []
        self.counter = 0
        self.event_dict = {"display": self.display_content, "event": self.event_content, "loop": self.event_content}
        return

    # disperse action into the correct list based on types value
    def insert_actions(self,a):
        if "display" in a.types:
            self.display_content.append(a)
            print("Item: ", a.name, " added to display content.")
        elif "event" in a.types:
            self.event_content.append(a)
            print("Item: ", a.name, " added to event content.")
        elif "loop" in a.types:
            self.loop_content.append(a)
            print("Item: ", a.name, " added to loop content.")
        return


    def insert_entity(self,content):
        for i in content.actions:
            self.insert_actions(i)
        return


    def condition_to_act(self, event):
        if self.entity_state == None:
            return False
        if self.active == None:
            return False
        if event == False:
            return False
        return True


    def act(self, event):
        if self.condition_to_act(event):
            return True


    # loop through the material in each list constantly, waiting for a change in events, blits, etc.
    def loop(self):
        while self.active:
            events = pygame.event.get()
            for e in events:
                for a in self.event_content:
                    a.act(e)
            for a in self.loop_content:
                a.act(None)
            for a in self.display_content:
                a.act(None)
        return


    # turn loop into dictionary app so that you can categorize events more effectively
    def loopv2(self):
        while self.active:
            events = pygame.event.get()
            for e in events:
                for a in self.event_dict:
                    try:
                        self.event_dict.get(a).act(e)
                    except:
                        self.event_dict.get(a).act(None)
        return