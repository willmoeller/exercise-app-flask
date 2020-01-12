from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from app.main.routes import main_blueprint
    app.register_blueprint(main_blueprint)

    # @app.route('/')
    # def index():
    #     return 'Hello World!'

    return app
