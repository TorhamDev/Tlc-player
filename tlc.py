from time import sleep
from Player.core import Player
from Player.info import show_track_info
from optparse import OptionParser
from rich.console import Console
from rich import print
parser = OptionParser()
(options, args) = parser.parse_args()

console = Console()

def handle_dirs(path:str):
    tracks = [os.path.join(path,i) for i in os.listdir(path)]
    tracks = [i for i in filter(lambda x: x if os.path.isdir(x) else None,tracks)] # To remove possible dirs
    return tracks

def get_status_data():
    current_time = player.get_current_playtime()
    if player.is_played:
        symbol_play = u"\u25b6"
    symbol_play = u"\u23f8"

    return f"[bold green]{current_time} <=> {player.get_total_media_time()} " + symbol_play


def main():
    try:
        with console.status(get_status_data()) as status:
            while player.is_played:
                sleep(0.6)
                status.update(get_status_data())
    except KeyboardInterrupt:
        print('Bye! :vulcan_salute:')

if __name__ == "__main__":
    # create player obj and show media info
    if os.path.isdir(args[0]):
        tracks = handle_dirs(args[0])
        additional = f"[deep_pink4]{args[0]}[/deep_pink4]"
        for track in tracks:
            player = Player(args[0],additional)
            show_track_info(player.media_load_info, player.tag)
            player.play()
    player = Player(args[0])
    show_track_info(player.media_load_info, player.tag)
    player.play()
    main()
