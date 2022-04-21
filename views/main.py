from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/main', methods=['GET', 'POST'])
def main_page() :
    return render_template('main.html')