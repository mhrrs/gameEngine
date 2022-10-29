import pygame, sys
from pygame.locals import *
import os
import random

# adding folders/ MAKE SURE YOU ARE IN THE CORRECT LOCATION
sys.path.append('C://Users//Michael Harris//Desktop//Masters CS//Clemson MSCS//2D_gameEngineConstruction//whackabox//engineThree//engine')

import actor as ac
import play as pl
import ui as ui
import utility as util
import sound as snd

class generate_message_action(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.children = []
        self.total = 0
        self.success = 0
        self.name = "gen_message"

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.generate_message(data)

    def generate_message(self, data):
        # pass values of counter entities to hud_action
        self.total = self.children[0].counter
        self.success = self.children[1].counter


class move_action(object):
    def __init__(self):
        self.entity_state = None
        self.types = ["event"]
        self.name = "move_rect"
        self.active = False
        self.children = []

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        if self.entity_state.active == False:
            return False
        if self.active == True:
            return True
        if data.type == MOUSEBUTTONDOWN:
            pos = data.pos
            return self.entity_state.is_inside(pos)
        return False

    def act(self, data):
        if self.condition_to_act(data):
            self.move(data)

    def move(self,data):
        for i in self.children:
                i.act(data)

        x = random.choice(range(50,1100))
        y = random.choice(range(50,600))
        box = 50
        self.entity_state.dimensions = (x,y,box,box)
        self.entity_state.color = (random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255)))


def main():
    pygame.init()

    # display window
    viewer = pl.frameViewerEntity(title = "whackabox", name = "Whackabox Window")
    viewer.insert_action(pl.make_terminate_action())
    display = pl.make_frameViewerAction()

    # init and add generate_message and draw_hud to HUD entity
    hud = util.make_hud_entity()
    hud_action = util.make_hud_action()
    hud.insert_action(hud_action)
    gen_message = generate_message_action()
    hud.insert_action(gen_message)

    # init timer entity
    timer_entity = util.make_timer_entity()
    update_timer_action = util.make_updateTimer_action()
    move_box = move_action()
    update_timer_action.children.append(move_box)

    # init alarm and timer and add start_timer functionality to alarm
    timer_start_action = util.make_startTimer_action()
    alarm_timer_action = util.make_alarmTimer_action()
    alarm_timer_action.children.append(timer_start_action)

    # #init sound and add to alarm timer
    alarm_sound_action = snd.make_box_hit_sound()
    alarm_timer_action.children.append(alarm_sound_action)
    update_timer_action.children.append(alarm_timer_action)

    # add easier functionality to change the alarm_countdown
    decrement_countdown_action = util.decrement_countdown_action()
    decrement_countdown_action.children.append(alarm_timer_action)

    # adding actions to entity
    timer_entity.insert_action(update_timer_action)
    timer_entity.insert_action(alarm_sound_action)
    timer_entity.insert_action(timer_start_action)
    timer_entity.insert_action(alarm_timer_action)
    timer_entity.insert_action(decrement_countdown_action)

    # button creation
    dimensions = (random.choice(range(50,400)),random.choice(range(50,400)),50,50)
    color = (random.choice(range(0,255)),random.choice(range(0,255)),random.choice(range(0,255)))
    button = ui.make_basic_button(dimensions,color)
    button.insert_action(ui.make_button_draw())
    button.insert_action(ui.make_color_change())
    press_action = ui.make_button_pressed()

    # init counter entities
    success_entity = util.make_success_counter()
    success_increment = util.make_increment_action()
    success_entity.insert_action(success_increment)
    total_entity = util.make_total_counter()
    total_increment = util.make_increment_action()
    total_entity.insert_action(total_increment)
    
    # add entities to generate_message action to adopt counter values
    gen_message.children.append(total_entity)
    gen_message.children.append(success_entity)

    # insert success and total counter actions into press_action in order to update entities
    press_action.children.append(success_increment)
    move_box.children.append(total_increment)
    
    #timer start after button has been pressed
    press_action.children.append(timer_start_action)

    # insert activate/deactivate utility functions into button class as actions
    button.insert_action(util.make_deactive())
    button.insert_action(util.make_active())

    # init and insert sound action into button and press_action
    sound_action = snd.make_box_hit_sound()
    button.insert_action(sound_action)
    press_action.children.append(sound_action)
    button.insert_action(press_action)

    # insert move-action into button
    button.insert_action(move_box)

    # insert hud into frameviewer action
    display.insert_entity(hud)

    # insert buttonEntity into frameviewer action
    display.insert_entity(button)

    # inserting window into frameviewer entity
    viewer.insert_action(display)

    # adding entities to game_content
    game_content = [viewer]
    game_content.append(timer_entity)
    game_content.append(button)

    # run game loop
    game = pl.make_gameLoopAction(game_content)
    game.loop()

main()