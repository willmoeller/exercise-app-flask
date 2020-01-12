from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from app.main.routes import main_blueprint
    app.register_blueprint(main_blueprint)

    from app.workouts.routes import workouts_blueprint
    app.register_blueprint(workouts_blueprint)

    # @app.route('/')
    # def index():
    #     return 'Hello World!'

    return app
