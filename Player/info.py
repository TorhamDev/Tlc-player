from rich import print
from rich.panel import Panel
from os import get_terminal_size
import datetime
terminal_column = get_terminal_size().columns


def show_track_info(load_info_obj, tag, path_file):
    """
    show track information

    params : `load_info_obj` : eyed3 load object
    params : `tag` : eyed3 tag object
    params : `path_file` : music path file
    """

    load_info = load_info_obj
    try:
        print(Panel(f"[dark_orange]{tag.title}[/dark_orange]".center(int(terminal_column)+25), title="Track Name"))  # noqa

        track_information = ''
        track_information += f"[deep_pink4]Playing From [/deep_pink4]: [gold3]{path_file}[/gold3]"+"\n"  # noqa
        track_information += "[deep_pink4]Track Artist[/deep_pink4]:   {}\n".format(tag.artist)  # noqa
        track_information += "[deep_pink4]Track Album[/deep_pink4]:    {}\n".format(tag.album)  # noqa
        track_information += "[deep_pink4]Track Duration[/deep_pink4]: {}\n".format(str(datetime.timedelta(seconds=load_info.info.time_secs)).split('.')[0])  # noqa
        track_information += "[deep_pink4]Track Number[/deep_pink4]:   {}\n".format(f"{tag.track_num[0]}/{tag.track_num[1]}")  # noqa
        track_information += "[deep_pink4]Track BitRate[/deep_pink4]:  {}\n".format(load_info.info.bit_rate[1])  # noqa
        track_information += "[deep_pink4]Track BitRate[/deep_pink4]:  {}\n".format(load_info.info.bit_rate_str)  # noqa
        track_information += "[deep_pink4]Sample Rate[/deep_pink4]:    {}\n".format(load_info.info.sample_freq)  # noqa
        track_information += "[deep_pink4]Mode[/deep_pink4]:           {}\n".format(load_info.info.mode)  # noqa
        print(Panel(track_information, title="Track Information"))
    except AttributeError:
        print(Panel(track_information, title="Track Information"))

    lyrics = u"".join([i.text for i in tag.lyrics])
    print(Panel(str(lyrics), title="Lyrics"))
