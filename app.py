"""
This module contains a Flask application which completes
the download of a youtube video as well as the querying of
certain videos.
"""

from urllib.parse import unquote
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from pytube import YouTube
from pytube.exceptions import RegexMatchError

app = Flask(__name__, template_folder="templates")
CORS(app)


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


@app.route("/download")
def download():
    """
    Downloads a YouTube video
    :return: Video as mp4
    """
    url = request.args.get("url")
    url = unquote(url)
    try:
        yt = YouTube(url)
        video_url = yt.streams.get_highest_resolution().url
        return jsonify({"video": video_url})
    except RegexMatchError as e:
        print("Error:", e)
        return jsonify({"video": "No video found."})
    except Exception as e:
        print("Error:", e)
        return jsonify({"video": "An error occurred."})



if __name__ == "__main__":
    app.run()
