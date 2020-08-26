import argparse
import connexion
from qcetlapi import api
from gsiqcetl.api import QCETLCache
from flask import render_template


def start_server():
    parser = argparse.ArgumentParser()
    parser.add_argument("cache_dir", help="Directory where gsiqcetl saves caches")
    args = parser.parse_args()

    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('api.yaml')
    # https://stackoverflow.com/questions/53941243/how-to-pass-a-variable-into-connexion-flask-app-context
    app.app.config['cache'] = QCETLCache(args.cache_dir)

    @app.route("/")
    def home():
        return render_template("index.html", version=api.etl_version())

    app.run(port=8080)
