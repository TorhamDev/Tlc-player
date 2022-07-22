from time import sleep
from Player.core import Player
from Player.info import show_track_info
from optparse import OptionParser
from rich.console import Console
from rich import print
from pynput import keyboard
from utils.keyboard_shortcut import keyboard_shortcut_handler
import os

# default track play numbers
current_track = 1
all_tacks_sum = 1


keys_currently_pressed = []


def on_press(key) -> None:
    """
    on keyboard keys pressed
    If the total of pressed keys is equal to 3
    it will be sent to keyboard_shortcut_handler for checking

    params : key : key pressed

    return None
    """
    if len(keys_currently_pressed) == 3:
        keys_currently_pressed.clear()

    if key not in keys_currently_pressed:
        keys_currently_pressed.append(key)

    if len(keys_currently_pressed) == 3:
        keyboard_shortcut_handler(player, keys_currently_pressed)


def handle_dirs(path: str) -> list:
    """
    return list of a dir file

    params : `path` : dir path

    return : `list file in target dir`
    """

    tracks = [os.path.join(path, i) for i in os.listdir(path)]
    # To remove possible dirs
    tracks = [i for i in filter(lambda x: x if os.path.isfile(x) else None, tracks)]  # noqa
    return tracks


def get_status_data() -> str:
    """
    get status play data

    return : `play status string`
    """

    current_time = player.get_current_playtime()
    if player.is_played:
        symbol_play = u"\u25b6"
    else:
        symbol_play = u"\u23f8"

    return (
        f"[bold green]{current_time} <=> {player.get_total_media_time()} "
        + f"{current_track}/{all_tacks_sum} "
        + symbol_play)


def main() -> None:
    """
    main function for run music

    return : `None`
    """

    player.play()
    try:
        # Collect events until released
        with keyboard.Listener(on_press=on_press) as listener:

            with console.status(get_status_data()) as status:

                while not player.is_stoped:
                    player.check_status()
                    sleep(0.6)
                    status.update(get_status_data())

                print("\nEnd :sunglasses:")

            listener.join()

    except KeyboardInterrupt:
        print('Bye! :vulcan_salute:')
        quit()


if __name__ == "__main__":
    parser = OptionParser()
    (options, args) = parser.parse_args()
    console = Console()
    console.clear()
    if len(args) == 0:
        print(
            "[bold red]You must specify a path to file or dir like:[/bold red][blue]"
            " tlc.py ~/Music/something.mp3 "
            "or tlc.py ~/Music/ [/blue]"
        )
        quit()

    path_file = path_file = args[0]
    # if user input is a dir
    if os.path.isdir(args[0]):
        tracks = handle_dirs(args[0])
        all_tacks_sum = len(tracks)
        for track in tracks:
            console.clear()
            player = Player(track)
            show_track_info(
                player.media_load_info,
                player.tag,
                path_file,
            )
            main()
            current_track += 1
    else:
        # if user input just a music
        player = Player(args[0])
        show_track_info(player.media_load_info, player.tag, path_file)
        main()
