
# this initializes as False in active so that when it is turned on, it can begin drawing.
class manEntity(object):
    def __init__(self):
        self.actions = []
        self.entity_state = None
        self.name = "man_entity"
        self.verbose = False
        self.active = True
        self.stage = 0
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return