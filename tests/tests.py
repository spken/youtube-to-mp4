"""
This module contains tests for the app module.
"""

import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_privacy(client):
    response = client.get("/privacy")
    assert response.status_code == 200


def test_download(client):
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    response = client.get("/download?url=" + url)
    assert response.status_code == 200
    data = response.json
    assert "video" in data
    if data["video"] == "No video found.":
        assert False, "Video not found."
