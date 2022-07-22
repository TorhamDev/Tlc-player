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
        count = 0

        while self.media_player.is_playing():
            if count >= 1000:
                print("Unable to play media")
                exit()
            count += 1
            
        self.is_played,self.is_paused,self.is_stopped = True,False,False

    def pause(self) -> None:
        """
        Pauses Music, if it is already paused, it will resume it.
        """
        self.media_player.pause()
        self.is_played,self.is_paused,self.is_stopped = True,True,False

    def stop(self) -> None:
        """
        Stops Music.
        """
        self.media_player.stop()
        self.is_played,self.is_paused,self.is_stopped = False,False,True

    def get_current_playtime(self) -> str:
        milliseconds_playtime = self.media_player.get_time()
        currentTime = str(datetime.timedelta(milliseconds=milliseconds_playtime)).split('.')[0]  # noqa
        return currentTime

    def get_total_media_time(self) -> str:
        """
        Gets total media time

        Return : Total time
        """
        try:
            time_secs = self.media_load_info.info.time_secs
            return str(datetime.timedelta(seconds=time_secs)).split('.')[0]
        except AttributeError:
            return "00:00:00"
    
    def is_music_finished(self) -> bool:
        if self.media_player.get_state() == vlc.State.Ended:
            return True
        return False
    
    def is_music_paused(self) -> bool:
        if self.media.get_state() == vlc.State.Paused:
            return True
        return False
