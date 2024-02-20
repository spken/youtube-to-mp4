"""
This module tests the app module.
"""

import pytest
from youtube_to_mp4.app import app as flask_app

@pytest.fixture(name="app")
def fixture_app():
    """
    Initalize flask application
    """
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app


@pytest.fixture(name="client")
def fixture_client(app):
    """
    Gets the testing client
    """
    return app.test_client()


def test_index(client):
    """
    Tests the index GET
    """
    response = client.get("/")
    assert response.status_code == 200


def test_about(client):
    """
    Tests the about GET
    """
    response = client.get("/about")
    assert response.status_code == 200


def test_privacy(client):
    """
    Tests the privacy GET
    """
    response = client.get("/privacy")
    assert response.status_code == 200


def test_download(client):
    """
    Tests the video download
    """
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    response = client.get("/download?url=" + url)
    assert response.status_code == 200
    data = response.json
    assert "video" in data
    if data["video"] == "No video found.":
        assert False, "Video not found."
