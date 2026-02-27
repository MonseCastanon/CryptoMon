from flask import Blueprint, render_template
from app.services.cryptoService import get_top_cryptos

crypto_bp = Blueprint("crypto", __name__, url_prefix="/crypto")

@crypto_bp.route("/")
def crypto_dashboard():
    cryptos = get_top_cryptos()
    return render_template("crypto.html", cryptos=cryptos)
