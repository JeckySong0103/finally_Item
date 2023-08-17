
import os
import cv2
import numpy as np
from PIL import Image

def gen_foreground(img_path, mask_path, res_path):
    img = cv2.imread("E:/photo/test-0005_nsd-00671.png")
    mask = cv2.imread("E:/photo/masks/15.png", 0)
    #back = cv2.imread("E:/photo/background.jpg")
    height, width, channel = img.shape
    b, g, r = cv2.split(img)
    res = np.zeros((4, height, width), dtype=img.dtype)
    res[0][0:height, 0:width] = b
    res[1][0:height, 0:width] = g
    res[2][0:height, 0:width] = r
    res[3][0:height, 0:width] = mask
    cv2.imwrite("E:/photo/hebing/15.jpg", cv2.merge(res))

if __name__ == "__main__":
    #gen_foreground(img_path, mask_path, res_path)
    gen_foreground("img.png", "mask.png", "res.jpg")



