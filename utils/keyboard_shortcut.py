from pynput.keyboard import Key


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
