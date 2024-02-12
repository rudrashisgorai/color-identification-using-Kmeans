
# Color Identification using KMeans

## Project Overview

This project is an API for color identification using the KMeans clustering algorithm. It allows users to upload an image and specify the number of dominant colors to identify. The application employs scikit-learn for machine learning and FastAPI for web service development.

## Features

- **Dominant Color Identification**: Identifies a specified number of dominant colors in an uploaded image.
- **HEX Color Codes Conversion**: Converts dominant colors into HEX codes.
- **FastAPI Integration**: Leverages FastAPI for efficient web service development.
- **Support for Basic Image Processing**: Includes functionalities like resizing and converting color spaces.

## Installation

To set up the project, ensure you have Python 3.6 or later. Follow these steps:

```bash
git clone https://github.com/rudrashisgorai/color-identification-using-Kmeans.git
cd color-identification-using-Kmeans
pip install -r requirements.txt
```

## Usage

To run the server:

```bash
uvicorn app:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`.

### Endpoint

- `POST /get-colors`: Upload an image to identify dominant colors. Parameters:
  - `NO_OF_COLORS`: Integer specifying the number of dominant colors to detect.
  - `file`: Image file (jpg or png format).

### Example

```python
import requests

url = 'http://127.0.0.1:8000/get-colors?NO_OF_COLORS=5'
files = {'file': ('pikachu.jpg', open('pikachu.jpg', 'rb'), 'image/jpeg')}  # Correct file and type
headers = {'accept': 'application/json'}  # Explicitly accept application/json

response = requests.post(url, files=files, headers=headers)  
print(response.json())
```

## Contributing

Your contributions are always welcome! Please check the [issues page](https://github.com/rudrashisgorai/color-identification-using-Kmeans/issues) for open issues or feel free to open a new one.

## Contact

Project Link: [https://github.com/rudrashisgorai/color-identification-using-Kmeans](https://github.com/rudrashisgorai/color-identification-using-Kmeans)
