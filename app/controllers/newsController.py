from flask import Blueprint, render_template
from app.services.newsService import get_crypto_news

news_bp = Blueprint("news", __name__, url_prefix="/news")

@news_bp.route("/")
def news():
    articles = get_crypto_news()

    return render_template(
        "news.html",
        articles=articles
    )