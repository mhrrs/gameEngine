

class headsUpEntity(object):
    def __init__(self):
        self.actions = []
        self.entity_state = None
        self.name = "hud_entity"
        self.verbose = False
        self.active = True
        self.counter = 0
        self.success_counter = 0
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return