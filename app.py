"""
This module contains a Flask application which completes
the download of a youtube video as well as the querying of
certain videos.
"""
# https://pytube.io/en/latest/user/quickstart.html

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():    
    """
    Renders index on application launch
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run()