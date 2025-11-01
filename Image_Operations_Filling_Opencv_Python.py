"""Wrapper to call package image operations; kept for compatibility."""

import argparse
import os
import cv2
from autonomous_lane_assist_system import image_ops


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Path to image file", default=None)
    args = parser.parse_args()

    if args.path is None:
        # attempt to find a sample next to the package
        sample = os.path.join(os.path.dirname(__file__), "Road_Sample_Image_Frame.jpeg")
        path = sample
    else:
        path = args.path

    img = image_ops.read_image(path)
    if img is None:
        print("Image not found:", path)
        return

    gray = image_ops.to_grayscale(img)
    blur = image_ops.gaussian_blur(img)
    edges = image_ops.canny_edges(blur)
    dil = image_ops.dilate(img)
    drawn, count = image_ops.find_and_draw_contours(img, edges)
    print("Found contours:", count)
    cv2.imshow("image", img)
    cv2.imshow("Gray", gray)
    cv2.imshow("Edges", edges)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 02:01:53 2025

@author: Adidas_07
"""

import cv2 as cv
import numpy as np
import math
import os
import matplotlib.pyplot as plt

image = cv.imread("C:\\Users\\Adidas_07\\Desktop\\Adidas_07\\Python_applications\\Road_Sample_Image_Frame.jpeg")
cv.imshow("image",image)

#Convert to grayScale Image
GRAY_scale_Image =cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray_Scale_Image",GRAY_scale_Image)

#Convert to Gausian Blur of the Image
Gaussian_Blur = cv.GaussianBlur(image, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Gaussian_Blur",Gaussian_Blur) 

#Canny Edge Detector 
canny= cv.Canny(Gaussian_Blur, 125, 175)
cv.imshow("CannyEdge Filter,",canny)

#Dilate the Image
dilate = cv.dilate(image, (3,3),3)
cv.imshow("Dilated Image",dilate)

#Contour Plot of an Image
contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

#Contour filling and edge detection
contour_fillling= cv.drawContours(image, contours, -1, (0, 0, 255), 2)
cv.imshow("Contour filling",contour_fillling)

#Curve Smoothening and gradient fill
#cv.approxPolyDP(curve, epsilon, closed)

cv.waitKey(0)

