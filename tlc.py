from time import sleep
from Player.core import Player
from utils.info import show_track_info
from utils.keyboard_shortcut import keyboard_shortcut_handler
from optparse import OptionParser
from rich.console import Console
from rich import print
from pynput import keybord
import os
# Default track play numbers
currentTrack = 1
allTrackSum = 1
keysCurrentlyPressed = []

def onPress(key) -> None:
    """
    Pressed keyboard keys
    If the total of pressed keys is equal to 3
    it will be sent to the keyboardShortcutHandler for handlation
    params : key : key preesed
    retrun None
    """
    if len(keysCurrentlyPressed) == 3:
        keysCurrentlyPressed.clear()

    if key not in keysCurrentlyPressed:
        keysCurrentlyPressed.append(key)

    if len(keysCurrentlyPressed) == 3:
        keyboardShortcutHandler(player, keysCurrentlyPressed)

def handleDirs(path: str) -> list:
    """
    Returns music tracks from a target dir

    params : `path` : dir path

    retrun : `music tracks in target dir`
    """

    tracks = [os.path.join(path, i) for i in os.listdir(path)]
    # To remove possible dirs
    tracks = [i for i in filter(lambda x: x if os.path.isfile(x) else None, tracks)]  # noqa
    return tracks

def getStatusData() -> str:
    """
    Returns play data status

    return : `play data status string`
    """

    current_time = player.get_current_playtime()
    if player.is_played:
        symbol_play = u"\u25b6"
    symbol_play = u"\u23f8"

    return (
        f"[bold green]{current_time} <=> {player.get_total_media_time()} "
        + f"{current_track}/{all_tacks_sum} "
        + symbol_play)

def playForFiles(path:str):
    """ 
    Plays tracks for music paths
    params : `path` : music path
    """
    player = Player(path)
    show_track_info(player.media_load_info, player.tag, path_file)
    main()

def playForDirs(path:str):
    """
    Plays tracks for dirs

    params : `path` : directory
    """
    tracks = handle_dirs(path)
    allTracksSum = len(tracks)
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

if __name__ == "__main__":
    parser = OptionParser()
    (option, args) = parser.parse_args()
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
    if os.path.isdir(args[0]):
        playForDirs(args[0])
    playforFiles(args[0])
