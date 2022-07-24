from pynput.keyboard import Key


class GoNext(object):
    def __init__(self, go_next=None) -> None:
        self.go_next = go_next

    def get(self):
        if self.go_next != None and self.go_next == True:
            return True
        else:
            return False


go_next = GoNext(go_next=False)


def keyboard_shortcut_handler(player_object, key_pressed: list) -> None:
    """
    keybboard shortcut handler for play, pause and ...

    params : player_object : player object for contorol media
    params : key_pressed : list of key pressed

    retru : None
    """
    if key_pressed[0] == Key.ctrl and str(key_pressed[1]) == "'b'":
        
        # pause handler
        if key_pressed[2] == Key.space:
            player_object.pause()

        elif key_pressed[2] == Key.right:
            go_next.go_next = True
    
    else:
        return False


def go_next_music() -> bool:
    if go_next.get() == False:
        return False

    elif go_next.get() == True:
        go_next.go_next = False
        return True
