
class hangerEntity(object):
    def __init__(self):
        self.actions = []
        self.entity_state = None
        self.name = "hang_entity"
        self.verbose = False
        self.active = True
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return