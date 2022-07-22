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
        self.mediaPath = mediaPath
        self.mediaPlayer = vlc.MediaPlayer()
        self.media = vlc.Media(self.mediaPath)
        self.mediaPlayer.set_media(self.media)
        self.tag = id3.Tag()
        self.tag.parse(self.mediaPath)
        self.mediaLoadInfo = load(self.mediaPath)
        self.isPlayed,self.isPaused,self.isStopped = False,False,False

    def start(self) -> None:
        """
        Plays Music.
        """
        self.media_player.play()
        self.isPlayed,self.isPaused,self.isStopped = True,False,False

    def pause(self) -> None:
        """
        Pauses Music
        """
        self.media_player.pause()
        self.isPlayed,self.isPaused,self.isStopped = False,True,False

    def stop(self) -> None:
        """
        Stops Music.
        """
        self.media_player.stop()
        self.isPlayed,self.isPaused,self.isStopped = False,False,True

    def getCurrentPlaytime(self) -> str:
        millisecondsPlaytime = self.media_player.get_time()
        currentTime = str(datetime.timedelta(milliseconds=milliseconds_playtime)).split('.')[0]  # noqa
        return currentTime

    def get_total_media_time(self) -> str:
        """
        Gets total media time

        Return : Total time
        """

        try:
            timeSecs = self.mediaLoadInfo.info.timeSecs
            return str(datetime.timedelta(seconds=timeSecs)).split('.')[0]
        except AttributeError:
            return "00:00:00"
