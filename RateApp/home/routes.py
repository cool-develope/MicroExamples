from flask import Blueprint, render_template
from flask import current_app as app
from RateApp.api import fetch_products

# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    products = fetch_products(app)
    return render_template(

    )