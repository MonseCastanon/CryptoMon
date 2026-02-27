from flask import Blueprint, render_template
from app.services.videosService import get_crypto_videos

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def index():
    videos = get_crypto_videos()
    return render_template("index.html", videos=videos)
