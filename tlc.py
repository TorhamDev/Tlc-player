from time import sleep
from Player.player import Player
from utils.info import show_track_info
from utils.keyboard_shortcut import keyboard_shortcut_handler, go_next_music
from optparse import OptionParser
from rich.console import Console
from rich import print
from pynput import keyboard
import os

# Default track play numbers
current_track = 1
all_tracks_sum = 1
keys_currently_pressed = []


def on_press(key, player) -> None:
    """
    Pressed keyboard keys
    If the total of pressed keys is equal to 3
    it will be sent to the keyboardShortcutHandler for handlation
    params : key : key preesed
    retrun None
    """
    if len(keys_currently_pressed) == 3:
        keys_currently_pressed.clear()

    if key not in keys_currently_pressed:
        keys_currently_pressed.append(key)

    if len(keys_currently_pressed) == 3:
        result = keyboard_shortcut_handler(player, keys_currently_pressed)
        if result == False:
            keys_currently_pressed.clear()
            print(keys_currently_pressed)


def handle_dirs(path: str) -> list:
    """
    Returns music tracks from a target dir

    params : `path` : dir path

    retrun : `music tracks in target dir`
    """

    tracks = [os.path.join(path, i) for i in os.listdir(path)]
    # To remove possible dirs
    tracks = [i for i in filter(lambda x: x if os.path.isfile(x) else None, tracks)]  # noqa
    return tracks


def get_status_data(player, all_tracks_sum, current_track) -> str:
    """
    Returns play data status
    params: `player` : player object
    return : `play data status string`
    """

    current_time = player.get_current_playtime()
    if player.is_music_paused():
        symbol_play = u"\u23f8"
    else:
        symbol_play = u"\u25b6"

    return (
        f"[bold green]{current_time} <=> {player.get_total_media_time()} "
        + f"{current_track}/{all_tracks_sum} "
        + symbol_play)


def play_for_files(path: str):
    """ 
    Plays tracks for music paths
    params : `path` : music path
    """
    main(path)


def play_for_dirs(path: str):
    """
    Plays tracks for dirs
    params : `path` : directory
    """
    tracks = handle_dirs(path)
    all_tracks_sum = len(tracks)
    current_track = 1
    for track in tracks:
        main(track, all_tracks_sum, current_track)
        current_track += 1


def main(track, track_sum: int = 1, current_track: int = 1):
    """ Main function for tlc
    params: `track` : Music path
    """
    player = Player(track)
    player.start()
    try:
        with console.screen() as screen:
            screen.console.clear()
            show_track_info(player.media_load_info, player.tag, path_file)
            with keyboard.Listener(on_press=lambda event: on_press(event, player)) as listener:
                with console.status(get_status_data(player, track_sum, current_track)) as status:
                    while not player.is_music_finished():
                        if go_next_music():
                            player.stop()
                            break
                        status.update(
                            get_status_data(
                                player,
                                track_sum,
                                current_track
                            )
                        )
                        sleep(0.6)
                listener.stop()
    except KeyboardInterrupt:
        print("Bye ! :vulcan_salute:")
        quit()


if __name__ == "__main__":
    parser = OptionParser()
    (option, args) = parser.parse_args()
    console = Console()
    if len(args) == 0:
        print(
            "[bold red]You must specify a path to file or dir like:[/bold red][blue]"
            " tlc.py ~/Music/something.mp3 "
            "or tlc.py ~/Music/ [/blue]"
        )
        quit()
    path_file = path_file = args[0]
    if os.path.isdir(args[0]):
        play_for_dirs(args[0])

    play_for_files(args[0])
