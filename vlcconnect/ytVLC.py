from typing import Tuple, Dict

import vlc
import youtube_dl

class VLCPlayer:
    """Create a VLC Player object"""

    def __init__(self) -> None:
        self.is_playing = False
        self.vlc_playlist = {}
        self.vlc_instance = vlc.Instance()
        self.vlc_player = self.vlc_instance.media_player_new()

    def add_to_playlist(self, media_key: str, media_info: Dict[str, str]) -> None:
        self.vlc_playlist[media_key] = media_info

    def play_selected_media(self, media_key: str=None) -> None:
        if media_key:
            if self.has_media():
                self.stop()

            self.vlc_player.set_fullscreen(True)
            video = self.vlc_playlist[media_key]["video"]
            # audio url string needs to be encoded to work
            # with vlc both on Windows and Linux
            audio = self.vlc_playlist[media_key]["audio"].encode()

            self._set_new_media(video, audio)

        self.vlc_player.play()
        self.is_playing = True

    def has_media(self) -> bool:
        return bool(self.vlc_player.get_media())

    def pause(self) -> None:
        self.vlc_player.pause()
        self.is_playing = False

    def stop(self) -> None:
        self.vlc_player.stop()
        self.is_playing = False

    def _set_new_media(self, video_url: str, audio_url: str) -> None:
        video_instance = self.vlc_instance.media_new(video_url)
        video_instance.slaves_add(vlc.MediaSlaveType.audio, 1, audio_url)

        self.vlc_player.set_media(video_instance)


def get_url_info(url: str, quality: str) -> Dict[str, str]:
    ydl_opts = {"format":f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(url, download=False)
    print(results["format"])
    video, audio = results["requested_formats"]
    return {
        "url": url, 
        "quality": quality, 
        "thumbnail": results["thumbnail"],
        "title": results["title"],
        "video": video["url"],
        "audio": audio["url"]
        }
