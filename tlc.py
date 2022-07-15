from time import sleep
from Player.core import Player
from Player.info import show_track_info
from optparse import OptionParser
from rich.console import Console
from rich import print

parser = OptionParser()
(options, args) = parser.parse_args()

console = Console()

# create player obj and show media info
if len(args) == 0:
    print("[bold red]You must specify a path to file like:[/bold red][blue] python tlc.py ~/Music/something.mp3[/blue]")
    quit()
player = Player(args[0])
show_track_info(player.media_load_info, player.tag)
player.play()


def get_status_data():

    current_time = player.get_current_playtime()

    if player.is_played:
        symbol_play = u"\u25b6"
    else:
        symbol_play = u"\u23f8"

    return f"[bold green]{current_time} <=> {player.get_total_media_time()} " + symbol_play


def main():
    try:
        with console.status(get_status_data()) as status:
            while player.is_played:
                sleep(0.6)
                status.update(get_status_data())
    except KeyboardInterrupt:
        print('Bay :vulcan_salute:')

main()
