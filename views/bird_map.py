from flask import Blueprint, render_template

bird_map = Blueprint('bird_map', __name__)

@bird_map.route('/main/bird-map', methods=['GET', 'POST'])
def show_googlemap() :
    return render_template('map.html')