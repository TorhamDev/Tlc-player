from config import FIRST_KEY, SECOND_KEY, PAUSE_BUTTON, NEXT_BUTTON


class GoNext(object):
    """
    an object for saving next value
    """

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
    if key_pressed[0] == FIRST_KEY and str(key_pressed[1]) == f"'{SECOND_KEY}'":

        # pause handler
        if key_pressed[2] == PAUSE_BUTTON:
            player_object.pause()

        # next handler
        elif key_pressed[2] == NEXT_BUTTON:
            go_next.go_next = True

    else:
        return False


def go_next_music() -> bool:
    """
    Checking if it is necessary to go to the next music?

    retrun : `True if next`
    """
    if go_next.get() == False:
        return False

    elif go_next.get() == True:
        go_next.go_next = False
        return True
