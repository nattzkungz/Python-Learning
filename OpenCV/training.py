import numpy as np
from PIL import Image as image
import os, cv2

def train_classifier(data_dir):
    path = [os.path.join(data_dir,i) for i in os.listdir(data_dir)]
    faces = []
    ids=[]
    for img in path:
        imgs = image.open(img).convert("L")
        imageNp = np.array(imgs, "uint8")
        id=int(os.path.split(img)[1].split(".")[1])
        faces.append(imageNp)
        ids.append(id)

    ids = np.array(id)
    


train_classifier("data")