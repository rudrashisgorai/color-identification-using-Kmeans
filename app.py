from sklearn.cluster import KMeans
import numpy as np
from collections import Counter
from PIL import Image
from io import BytesIO
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


def RGB2HEX(color):
    """Convert RGB color to HEX format."""
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def flatten(image_array):
    """Flatten a 3D image array to 2D."""
    return image_array.reshape(image_array.shape[0] * image_array.shape[1], 3)


def read_imagefile(file) -> Image.Image:
    """Read image file as PIL Image."""
    return Image.open(BytesIO(file))


def extract_colors(n_colors, image_array):
    """Extract N most dominant colors from an image."""
    try:
        clf = KMeans(n_clusters=n_colors)
        labels = clf.fit_predict(image_array)
        counts = Counter(labels)
        center_colors = clf.cluster_centers_
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
        return hex_colors
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


@app.post("/get-colors")
async def get_colors(no_of_colors: int, file: UploadFile = File(...)):
    """API endpoint to extract dominant colors from an uploaded image."""
    try:
        if file.content_type not in ["image/jpeg", "image/png"]:
            return {"error": "Image must be in JPEG or PNG format."}

        image = read_imagefile(await file.read())
        image = image.convert("RGB")  # Ensure image is in RGB format

        image = image.resize((100, 100))  # Resize for faster processing

        image_array = np.array(image)
        flattened_image_array = flatten(image_array)

        dominant_colors = extract_colors(no_of_colors, flattened_image_array)
        if dominant_colors:
            return {"dominant_colors": dominant_colors}
        else:
            return {"error": "Could not determine dominant colors."}
    except Exception as e:
        return {"error": str(e)}
