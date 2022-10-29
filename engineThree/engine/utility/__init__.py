
def make_active():
    import utility.action.activ as activ
    result = activ.activate()
    return result

def make_deactive():
    import utility.action.deactiv as deactiv
    result = deactiv.deactivate()
    return result

def make_hud_entity():
    import utility.entity.hudEntity as hue
    res = hue.headsUpEntity()
    return res

def make_hud_action():
    import utility.action.hudAction as hud
    res = hud.drawHudAction()
    return res

def make_increment_action():
    import utility.action.incrementCounterAction as inc
    res =  inc.incrementAction()
    return res

def make_success_counter():
    import utility.entity.successCounterEntity as suc
    return suc.susCounterEntity()

def make_total_counter():
    import utility.entity.totalCounterEntity as tot
    return tot.totCounterEntity()

def make_timer_entity():
    import utility.entity.timerEntity as etime
    res =  etime.timerEntity()
    return res

def make_startTimer_action():
    import utility.action.startTimer as stime
    res = stime.startTimerAction()
    return res

def make_updateTimer_action():
    import utility.action.updateTimer as utime
    res = utime.updateTimerAction()
    return res

def make_alarmTimer_action():
    import utility.action.alarmTimer as atime
    res = atime.alarmTimerAction()
    return res

def decrement_countdown_action():
    import utility.action.decrementCountdown as dectime
    res = dectime.decrementCountdownAction()
    return res