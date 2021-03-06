from flask import Blueprint, render_template, request
from .ytVLC import VLCPlayer, get_url_info

views = Blueprint("views", __name__)

vlc_player = VLCPlayer()

@views.route("/", methods=["GET", "POST"])
def home():
    qualities = ["144", "240", "360", "480", "720", "1080"]
    playlist = vlc_player.vlc_playlist

    if request.method == "POST":
        link = request.form.get("query")
        control = request.form.get("control_button")
        playlist_req = request.form.get("playlist_button")

        if link:
            selected_quality = request.form.get("vid_quality")
            media_handler(link, selected_quality)
        elif control:
            control_handler(control)
        elif playlist_req:
            playlist_handler(playlist_req)

        is_playing = vlc_player.is_playing

        return render_template("home.html", qualities=qualities, is_playing=is_playing, playlist=playlist)
    else:
        return render_template("home.html", qualities=qualities, playlist=playlist)

def media_handler(url: str, quality: str) -> None:
    url_info = get_url_info(url, quality)
    vlc_player.add_to_playlist(url, url_info)

    if not vlc_player.is_playing:
        vlc_player.play_selected_media(url)

def control_handler(control: str) -> None:
    if control == "play":
        vlc_player.play_selected_media()
    elif control == "pause":
        vlc_player.pause()
    elif control == "stop":
        vlc_player.stop()

def playlist_handler(url: str) -> None:
    vlc_player.play_selected_media(url)
