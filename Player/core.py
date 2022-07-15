import vlc
import datetime
from eyed3 import id3, load


class Player(object):

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

    def get_media_path(self):
        return self.media_path

    def play(self):
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

    def pause(self):
        self.media_player.pause()
        self.is_paused = True
        self.is_played = False
        return True

    def check_status(self):
        playtime_check = int(self.get_current_playtime().split(':')[-1]) > 0  # noqa
        if self.media_player.is_playing() == 1 or not playtime_check:
            playtime_check = int(self.get_current_playtime().split(':')[-1]) > 0  # noqa
            self.is_played = True
            self.is_stoped = False
        else:
            self.is_played = False
            self.is_stoped = True

    def done(self):
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

    def get_total_media_time(self):
        try:
            time_secs = self.media_load_info.info.time_secs
            return str(datetime.timedelta(seconds=time_secs)).split('.')[0]
        except AttributeError:
            return "00:00:00"

    def get_total_media_time_as_seconds(self):
        return self.media_load_info.info.time_secs
