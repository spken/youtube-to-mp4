"""
This module contains a Flask application which completes
the download of a youtube video as well as the querying of
certain videos.
"""

from flask import Flask

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return "Hello, World"

# https://pytube.io/en/latest/user/quickstart.html


if __name__ == "__main__":
    app.run()