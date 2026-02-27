from flask import Blueprint, render_template, request
from app.services.videosService import search_videos

videos_bp = Blueprint("videos", __name__, url_prefix="/videos")

@videos_bp.route("/", methods=["GET"])
def videos():
    query = request.args.get("q", "cryptocurrency news")

    results = search_videos(query=query)

    return render_template(
        "videos.html",
        videos=results,
        query=query
    )