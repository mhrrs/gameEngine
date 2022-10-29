import random
# The purpose of this class is to change the color of an object during its existence

class colorChangeAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_button_action"
        self.active = True
        self.counter = 1
        self.new_color = [0,0,0]
        self.red = 0
        self.green = 0
        self.blue = 0
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        elif self.entity_state.active == False:
            return False
        if data == None:
            return False
        return True

    def act(self, event):
        if self.condition_to_act(event):
            self.change_color(event)
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

# linear implementation
    def change_color(self, event):
        object_color = self.entity_state.color
        self.counter += 1
        
        # convert tuple to list
        j = 0
        for i in object_color:
            if i + self.counter < 255:
                self.new_color[j] = i + self.counter
            else:
                self.new_color[j] = 0
                self.counter = 1
            j+=1

        print(self.new_color[0],self.new_color[1],self.new_color[2])
        self.entity_state.color = (self.new_color[0],self.new_color[1],self.new_color[2])


# interesting but not great
    def change_colorv2(self, event):
        object_color = self.entity_state.color
        self.counter += 1
        
        # translate colors to class
        self.red = object_color[0]
        self.green = object_color[1]
        self.blue = object_color[2]

        if int((self.red + self.counter)/2) < 255:
            self.red = (self.red + self.counter)/2
        if int((self.green + self.counter)/3) < 255:
            self.green = (self.green + self.counter)/3
        if int((self.blue + self.counter)/4) < 255:
            self.blue = (self.blue + self.counter)/4
            self.entity_state.color = (self.red, self.green, self.blue)
            print(self.red, self.green, self.blue)
            return
        
        print(self.red, self.green, self.blue)

        self.red = 0
        self.blue = 0
        self.gree = 0
        self.counter = 1
        return

# 3rd attempt at a better color changer
    def change_colorv3(self, event):
            object_color = self.entity_state.color
            self.counter += 1
            
            # translate colors to class
            self.red = object_color[0]
            self.green = object_color[1]
            self.blue = object_color[2]

            palette = [self.red,self.green,self.blue]

            acolor = random.choice(palette)
            
            if acolor + self.counter < 255:
                acolor += self.counter
                
            print(self.red, self.green, self.blue)
            self.entity_state.color = (self.red, self.green, self.blue)