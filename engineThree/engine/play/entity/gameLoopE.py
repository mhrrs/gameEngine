class gameLoopEntity(object):
    def __init__(self):
        self.actions = []
        self.name = "game_loop_entity"
        self.verbose = False
        self.active = True
        self.counter = 0
        return

    def insert_action(self, a):
        a.entity_state = self
        self.actions.append(a)
        return