from flask import Blueprint, render_template

workouts_blueprint = Blueprint('workouts', __name__, template_folder='templates')

@workouts_blueprint.route('/log/')
def log():
    workouts = {
        "workout 1": "run",
        "workout 2": "lift",
        "workout 3": "run" 
    }
    return render_template('log.html', workouts=workouts)
