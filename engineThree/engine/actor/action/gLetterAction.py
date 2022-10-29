import pygame
from pygame.locals import *
import time


class guessLetterAction(object):
    def __init__(self, word):
        self.types = ["event"]
        self.entity_state = None
        self.verbose = False
        self.word = word
        self.name = "active_letter_action"
        self.wrong_guesses = []
        self.guesses = []
        self.correct_guesses = []
        self.content_left = 100
        self.num_guesses = 7
        self.counter = 0
        return

    def condition_to_act(self,data):
        if self.entity_state == None:
            return False
        if self.entity_state.active == None:
            return False
        elif data.type != KEYDOWN:
            return False
        return True


    def act(self,data):
        if self.condition_to_act(data):
            self.letter_getter(data)

            # toggle active attribute to display the correct letter and remove correct box
            for i in self.word:
                if i in self.correct_guesses:
                    self.activator(str(i)+"_letter", True)
                    self.activator(str(i)+"_rect", False)
            
            for i in self.wrong_guesses:
                self.counter+=1
                self.activator(str(i)+"_al_letter", True)
            # self.counter = len(self.wrong_guesses)

            # turn word into a list of 0 dupes and check to see if game is still valid
            wordList = [*set([i for i in self.word])]
            if len(self.correct_guesses) == len(wordList):
                print("CONGRATS. You win.")
                self.success_game()

            if self.counter == self.num_guesses:
                self.failed_game()
                print("You have dishonored your family name.")
                print("guessed letters:", self.guesses)
                print("correctly guessed letters:", self.correct_guesses)

                
            self.counter = 0


    # used to change an entities state to True or False
    def activator(self, name, status):
        for x in self.entity_state.actions:
            if x.name == "frameViewerAction":
                for y in x.children:
                    if y.entity_state.name == name:
                        y.entity_state.active = status 
                    

    # recieves keyInput and pumps the letter into the check_letter function
    def letter_getter(self, data):
        self.verbose = True
        
        letter_dict = {
            K_a:"A", K_b:"B", K_c:"C", K_d:"D", K_e:"E",
            K_f: "F", K_g: "G", K_h: "H", K_i: "I", K_j: "J", K_k:"K", 
            K_l:"L", K_m: "M", K_n: "N", K_o:"O", K_p: "P", K_q: "Q",
            K_r:"R", K_s:"S", K_t: "T", K_u: "U", K_v: "V", K_w: "W", 
            K_x: "X", K_y: "Y", K_z: "Z"
        }

        if data.key in letter_dict:
            value = letter_dict.get(data.key)
            if value != None:
                self.check_letter(value)

            if self.verbose:
                print("Key ", value, " was pressed.")
        else:
            print("invalid character.")


    # receives a letter and appends it to the correct lists depending on the word
    def check_letter(self, data):
        letter = str.lower(data)
        if letter not in self.word:
            if letter not in self.wrong_guesses:
                self.wrong_guesses.append(letter)
                self.guesses.append(letter)
        else:
            if letter not in self.correct_guesses:
                self.correct_guesses.append(letter)
                self.guesses.append(letter)
                

    #display a failed game screen 
    def success_game(self):
        wordList = [*set([i for i in self.word])]
        for i in self.word:
            # remove all letters and rects in the guess-word area
            if i in wordList:
                self.activator(str(i)+"_letter", False)
                self.activator(str(i)+"_rect", False)
        #activate winGame letters 
        for i in "You win!":
            self.activator(str(i)+"_winGame", True)


    #display a failed game screen 
    def failed_game(self):
        wordList = [*set([i for i in self.word])]
        for i in self.word:
            # remove all letters and rects in the guess-word area
            if i in wordList:
                self.activator(str(i)+"_letter", False)
                self.activator(str(i)+"_rect", False)
        # activate endGame letters
        for i in "failed game.":
            self.activator(str(i)+"_endGame", True)