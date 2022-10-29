import pygame

class drawHudAction(object):
    def __init__(self):
        self.types = ["display"]
        self.entity_state = None
        self.verbose = False
        self.name = "draw_hud_action"
        self.children = []
        self.counter_state = None
        self.total = 0
        self.success = 0
        return

    def insert_children(self, a):
        a.entity_state = self
        self.children.append(a)
        return
    
    def condition_to_act(self, data):
        if self.entity_state == False:
            return False
        if data == None:
            return False
        return True

    def act(self, data):
        if self.condition_to_act(data):
            self.draw_hud(data)
        if self.verbose:
                print(self.name, " for ", self.entity_state.name)
        return

    def draw_hud(self, data):
        # this should reference the totalCounterEntity and successCounterEntity
        
        for i in self.entity_state.actions:
            if i.name == "gen_message":
                message = i

        hudDisplayFont = pygame.font.Font('freesansbold.ttf',10)
        hud_display = hudDisplayFont.render("Total: " + str(message.total),True, (255,255,255))
        hud_rect = pygame.draw.rect(data, (0,0,0), (10,10,50,50))
        data.blit(hud_display, hud_rect)
        hud_display = hudDisplayFont.render("Successful: " + str(message.success),True, (255,255,255))
        hud_rect = pygame.draw.rect(data, (0,0,0), (10,20,40,40))
        data.blit(hud_display, hud_rect)
