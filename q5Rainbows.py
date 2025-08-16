"""
File: q5Rainbows.py

This file contains the script for Question 5 of Homework 1

This program includes draws a grid of rainbows all over an input image.

Author: <your name here>
"""
# TODO: Put your name above!

import cv2


def drawRainbow(img, pos):
    """This takes in an image, an (x, y) position to center the rainbow on in the image. It draws a rainbow as a
    series of half-ellipses in decreasing sizes, each reducing the axis by 15."""
    # TODO: Modify this function to draw the half-ellipses instead of rectangles
    colors = [(22, 20, 232), (0, 165, 255), (54, 235, 250), (20, 195, 121),
              (231, 125, 72), (157, 54, 75), (157, 54, 112)]

    currAxis = 100
    (x, y) = pos
    cv2.rectangle(img, (x - 100, y - 100), (x + 100, y), colors[0], -1)


# -------------------------------------------------------------------------------------------------------
# Main script

# Read in large background picture
myIm = cv2.imread("../../Comp194-Code/SampleImages/landscape1.jpg")
hgt, wid, dep = myIm.shape

# Loop over x positions to draw rainbows at, and inside that loop over y positions to draw rainbows at
for x in range(150, wid, 250):
    for y in range(150, hgt, 250):
        drawRainbow(myIm, (x, y))
        cv2.imshow("Rainbows", myIm)
        cv2.waitKey(100)  # Special version of waitKey only waits 100 millisecs before going on

# Add a permanent wait at the end so we can see the final image as long as we like
cv2.waitKey()
