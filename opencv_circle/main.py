import cv2 as cv
import numpy as np


def rescale(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = width, height
    return cv.resize(frame, dimensions, interpolation=cv.INTER_LINEAR)


img = cv.imread("../textures/launch.bmp")
resized_img = rescale(img, 0.5)

blank = np.zeros(resized_img.shape[:2], dtype="uint8")
cv.imshow("Blank image", blank)

circle = cv.circle(blank, (resized_img.shape[1] // 2, resized_img.shape[0] // 2),
                   100, (255, 255, 255), -1)

cv.imshow("Circle", circle)

masked_image = cv.bitwise_and(resized_img, resized_img, mask=circle)
cv.imshow("Masked image", masked_image)

cv.imshow("Display window", resized_img)

k = cv.waitKey(0)  # Wait for a keystroke in the window
