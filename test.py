import cv2
import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()


folder = "/gui/images"

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images


load_images_from_folder("/gui/images")