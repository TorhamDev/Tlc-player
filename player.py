from eyed3 import id3,load
import eyed3
import datetime
import vlc
eyed3.log.setLevel("ERROR")


class Player():
    """
    Player object to control music.
    """
    def __init__(self,media_path) -> None:
        self.media_path = media_path
        self.media_player = vlc.MediaPlayer()
        self.media = vlc.Media(self.media_path)
        self.media_player.set_media(self.media)
        self.tag = id3.Tag()
        self.tag.parse(self.media_path)
        self.media_load_info = load(self.media_path)
        self.is_played,self.is_paused,self.is_stopped = False,False,False

    def start(self) -> None:
        """
        Plays Music.
        """
        self.media_player.play()
        self.is_played,self.is_paused,self.is_stopped = True,False,False

    def pause(self) -> None:
        """
        Pauses Music
        """
        self.media_player.pause()
        self.is_played,self.is_paused,self.is_stopped = False,True,False

    def stop(self) -> None:
        """
        Stops Music.
        """
        self.media_player.stop()
        self.is_played,self.is_paused,self.is_stopped = False,False,True

    def getCurrentPlaytime(self):
        millisecondsPlaytime = self.media_player.get_time()
        currentTime = str(datetime.timedelta(milliseconds=milliseconds_playtime)).split('.')[0]  # noqa
        return currentTime
