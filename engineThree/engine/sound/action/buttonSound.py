import pygame
from pygame.locals import *
from sound.action import *
import os
import random
import sys

# adding folders/ MAKE SURE YOU ARE IN THE CORRECT LOCATION
os.chdir(os.path.dirname(os.path.abspath(r'C:\Users\Michael Harris\Desktop\Masters CS\Clemson MSCS\2D_gameEngineConstruction\whackabox\engineThree\assets\sounds\assets_sounds_explosion.wav')))

class buttonSoundAction(object):
    def __init__(self):
        self.load_active = False
        self.types = ["event"]
        self.entity_state = None
        self.name = "play_sound_action"
        self.children = []
        self.active = False
        self.verbose = False
        self.sounds = ["Recording.mp3", "RecordingTwo.mp3", "RecordingThree.mp3", "game_wave_alarm.wav", "assets_sounds_explosion.wav"]
        return

    def condition_to_act(self, data):
        if self.active == False:
            return False
        if self.entity_state == None:
            return False
        return True

    def act(self, event):
        if self.condition_to_act(event):
            # insert action function for sound if button is pressed.
            self.play_sound()

            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def play_sound(self):
        print("sound entity: ", self.entity_state.name)
        if self.entity_state.name == "button_entity":
            # load song
            box_hit_sound = pygame.mixer.Sound(self.sounds[4])

            # play sound
            box_hit_sound.play()

        if self.entity_state.name == "timer_entity":
            # load song
            box_hit_sound = pygame.mixer.Sound(self.sounds[3])

            # play sound
            box_hit_sound.play()