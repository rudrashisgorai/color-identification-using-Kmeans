from sklearn.cluster import KMeans
#import matplotlib.pyplot as plt
import numpy as np


from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76

from fastapi import FastAPI, File, UploadFile
#import cv2
from PIL import Image
from io import BytesIO

app = FastAPI()


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

# def get_image(image_path):
#     image = cv2.imread(image_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     return image

def flatten(modified_image):
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    return modified_image

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

def colors(NO_OF_COLORS : int , image : np.ndarray):
    try:
        #modified_image = flatten(image)
        modified_image = image
        clf = KMeans(n_clusters = NO_OF_COLORS)
        labels = clf.fit_predict(modified_image)

        counts = Counter(labels)

        center_colors = clf.cluster_centers_

        ordered_colors = [center_colors[i] for i in counts.keys()]

        hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
        return hex_colors
    except Exception as e:
        print(e)



@app.post("/get-colors")
async def get_colors( NO_OF_COLORS: int ,file: UploadFile = File(...) ):
    try:
        extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
        if not extension:
            return "Image must be jpg or png format!"

        
        image = read_imagefile(await file.read())
        print(image.size)
        image = image.convert('RGB')
        image = image.resize((100 , 100))
        
        image = np.array(image)
        print(image.shape)
        image = flatten(image)
        print(image.shape)

        
        return colors(NO_OF_COLORS , image)


    except Exception as e :
        print(e)
        return f"{e}"



