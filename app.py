# -*- coding: utf-8 -*-
#
import flask
import mwoauth
import os
import yaml


app = flask.Flask(__name__)
application = app


# Load configuration from YAML file
__dir__ = os.path.dirname(__file__)
app.config.update(
    yaml.safe_load(open(os.path.join(__dir__, 'config.yaml'))))


@app.route('/')
def index():
	return flask.render_template('index.html')


if __name__ == "__main__":
	app.run(host="0.0.0.0")
