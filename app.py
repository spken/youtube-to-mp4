"""
This module contains a Flask application which completes
the download of a youtube video as well as the querying of
certain videos.
"""
# https://pytube.io/en/latest/user/quickstart.html

from flask import Flask, jsonify, render_template
from pytube import YouTube
import urllib

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
    """yt = YouTube(
        'http://youtube.com/watch?v=2lAe1cqCOXo',
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
        proxies=my_proxies,
        use_oauth=False,
        allow_oauth_cache=True
    )
    """
    decodedURL = urllib.parse.unquote(url)
    yt = YouTube(decodedURL)
    return jsonify({"title": yt.title})


if __name__ == "__main__":
    app.run()
