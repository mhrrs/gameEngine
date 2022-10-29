
class activate(object):
    def __init__(self):
        self.types = ["event"]
        self.entity_state = None
        self.verbose = False
        self.name = "activate_button"
        return

    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.activator()
            if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def activator(self):
        self.entity_state.active = True
        return
