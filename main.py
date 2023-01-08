import cv2
import numpy as np

image = cv2.imread('Road2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce high frequency noise
gray_blur = cv2.GaussianBlur(gray, (5,5), 0)

# Perform Canny edge detection
edges = cv2.Canny(gray_blur, 50, 150)

# Define the region of interest (ROI)
vertices = np.array([[(0,image.shape[0]), (450, 290), (490, 290), (image.shape[1],image.shape[0])]], dtype=np.int32)

# Create a mask
mask = np.zeros_like(edges)
cv2.fillPoly(mask, vertices, 255)
masked_edges = cv2.bitwise_and(edges, mask)

# Define the Hough transform parameters
rho = 2
theta = np.pi/180
threshold = 15
min_line_length = 40
max_line_gap = 20

# Run Hough on the edge-detected image
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)

# Iterate over the output "lines" and draw the lines on the image
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(image, (x1,y1), (x2,y2), (255,0,0), 5)

# Display the image
cv2.imshow('lane', image)
cv2.waitKey(0)
cv2.destroyAllWindows()