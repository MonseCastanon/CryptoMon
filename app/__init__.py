from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .controllers.homeController import home_bp
    from .controllers.cryptoController import crypto_bp
    from .controllers.newsController import news_bp
    from .controllers.videosController import videos_bp
    from .controllers.aboutController import about_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(crypto_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(videos_bp)
    app.register_blueprint(about_bp)

    return app
