from flask import Flask, render_template
from api.routes import api_bp
from config import Config

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    # Register API blueprint
    app.register_blueprint(api_bp, url_prefix="/api")

    # Serve frontend
    @app.route("/")
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
