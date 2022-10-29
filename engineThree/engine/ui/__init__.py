

def make_basic_button(bounds, color):
    import ui.entity.buttonEntity as bu
    result = bu.buttonEntity(bounds, color)
    return result

def make_button_draw():
    import ui.action.drawButton as db
    return db.drawRectButtonAction()

def make_button_pressed():
    import ui.action.pressButton as pb
    return pb.pressedButtonAction()
    
def make_color_change():
    import ui.action.colorChange as cc
    return cc.colorChangeAction()