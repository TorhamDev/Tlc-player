from time import sleep
from Player.core import Player
from Player.info import show_track_info
from optparse import OptionParser
from rich.console import Console
from rich import print
import os

parser = OptionParser()
(options, args) = parser.parse_args()

console = Console()


def handle_dirs(path: str) -> list:
    """
    retrun list of a dir file

    params : `path` : dir path

    retrun : `list file in target dir`
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

    return f"[bold green]{current_time} <=> {player.get_total_media_time()} " + symbol_play  # noqa


def main() -> None:
    """
    main function for run music

    return : `None`
    """

    player.play()
    try:
        with console.status(get_status_data()) as status:
            while player.is_played:
                player.check_status()
                sleep(0.6)
                status.update(get_status_data())
            print("\nEnd :sunglasses:")
    except KeyboardInterrupt:
        print('Bye! :vulcan_salute:')
        quit()


if __name__ == "__main__":

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
        for track in tracks:
            player = Player(track)
            show_track_info(
                player.media_load_info,
                player.tag,
                path_file,
            )
            main()
    else:
        # if user input just a music
        player = Player(args[0])
        show_track_info(player.media_load_info, player.tag, path_file)
        main()
