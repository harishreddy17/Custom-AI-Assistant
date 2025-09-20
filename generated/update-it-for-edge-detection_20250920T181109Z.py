import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)  # Convert to grayscale

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edges (Canny)', edges)

# Save the edge-detected image
cv2.imwrite('edges_canny.jpg', edges)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
