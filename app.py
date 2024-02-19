"""
This module contains a Flask application which completes
the download of a youtube video as well as the querying of
certain videos.
"""
# https://pytube.io/en/latest/user/quickstart.html

import urllib
from flask import Flask, jsonify, render_template
from pytube import YouTube

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    """
    Renders index on application launch
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Renders about page
    """
    return render_template("pages/about.html")


@app.route("/privacy")
def privacy():
    """
    Renders privacy policy page
    """
    return render_template("pages/privacy.html")


@app.route("/download/<url>")
def download(url):
    """
    Downloads a YouTube video
    :return: Video as mp4
    """
    decoded_url = urllib.parse.unquote(url)
    yt = YouTube(decoded_url)
    return jsonify({"title": yt.title})


if __name__ == "__main__":
    app.run()
