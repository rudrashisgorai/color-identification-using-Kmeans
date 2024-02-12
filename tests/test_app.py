from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Append the directory of app.py to the system path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # Now you can import app like this


client = TestClient(app)


def test_get_colors_with_valid_image():
    """
    Test the /get-colors endpoint with a valid image file.
    """
    url = "/get-colors"
    params = {"no_of_colors": 3}
    files = {"file": ("pikachu.jpg", open("../pikachu.jpg", "rb"), "image/jpeg")}
    response = client.post(url, files=files, params=params)

    assert response.status_code == 200
    assert "dominant_colors" in response.json()


def test_get_colors_with_invalid_image_format():
    """
    Test the /get-colors endpoint with an invalid image format.
    """
    url = "/get-colors"
    params = {"no_of_colors": 3}
    files = {"file": ("test.txt", "this is not an image", "text/plain")}
    response = client.post(url, files=files, params=params)

    assert response.status_code == 200  # Assuming your API handles this gracefully
    assert "error" in response.json()
    assert "Image must be in JPEG or PNG format." in response.json()["error"]


# Add more tests as needed
