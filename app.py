from flask import Flask
from config import Config

from routes.resume import resume_bp
from routes.analysis import analysis_bp

import os


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    os.makedirs(
        app.config["UPLOAD_FOLDER"],
        exist_ok=True
    )

    app.register_blueprint(resume_bp)
    app.register_blueprint(analysis_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)