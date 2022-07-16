import vlc
import datetime
from eyed3 import id3, load


class Player(object):
    """
    Making a player object to control music
    """

    is_played = False
    is_paused = False
    is_stoped = False

    def __init__(self, media_path) -> None:
        self.media_player = vlc.MediaPlayer()
        self.media_path = media_path
        self.media = vlc.Media(self.media_path)
        self.media_player.set_media(self.media)
        self.tag = id3.Tag()
        self.tag.parse(self.media_path)
        self.media_load_info = load(self.media_path)

    def get_media_path(self) -> str:
        """
        get media path

        retrun : `string of media path`
        """
        return self.media_path

    def play(self) -> bool:
        """
        play curren media
        retrun : `True if media played`
        """

        self.media_player.play()
        count = 0
        while self.media_player.is_playing():
            if count >= 1000:
                print("Unable to play media")
                exit()
            count += 1

        self.is_played = True
        self.is_paused = False
        return True

    def pause(self) -> bool:
        """
        pause current media

        return : `true if media paused`
        """
        self.media_player.pause()
        self.is_paused = True
        self.is_played = False
        return True

    def check_status(self) -> None:
        playtime_check = int(self.get_current_playtime().split(':')[-1]) > 0  # noqa
        if self.media_player.is_playing() == 1 or not playtime_check:
            playtime_check = int(self.get_current_playtime().split(':')[-1]) > 0  # noqa
            self.is_played = True
            self.is_stoped = False
        else:
            self.is_played = False
            self.is_stoped = True

    def done(self) -> bool:
        """
        stop media

        retrun : `true if media is doned`
        """
        self.media_player.stop()
        self.is_played = False
        self.is_paused = False
        self.is_stoped = True
        return True

    def get_current_playtime(self):
        milliseconds_playtime = self.media_player.get_time()
        current_time = str(datetime.timedelta(milliseconds=milliseconds_playtime)).split('.')[0]  # noqa

        return current_time

    def get_current_milliseconds_playtime(self):
        return self.media_player.get_time()

    def get_total_media_time(self) -> str:
        """
        get current media total time

        return : string of total time  
        """

        try:
            time_secs = self.media_load_info.info.time_secs
            return str(datetime.timedelta(seconds=time_secs)).split('.')[0]
        except AttributeError:
            return "00:00:00"

    def get_total_media_time_as_seconds(self) -> int:
        """
        get totla media as seconds

        retrun : int of seconds
        """
        return self.media_load_info.info.time_secs
