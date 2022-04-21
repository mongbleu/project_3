from flask import Flask
#factory 패턴

def create_app() :
    app = Flask(__name__)
    
    from .views.main import bp
    from .views.bird_map import bird_map
    app.register_blueprint(bp)
    app.register_blueprint(bird_map)
    
    return app


if __name__ == "__main__" :
    app = create_app()
    app.run()