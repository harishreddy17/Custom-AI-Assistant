
import cv2

# Load the image
image = cv2.imread('test.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Display the original image
    cv2.imshow('Original Image', image)

    # Apply Gaussian Blur (smoothing)
    # Parameters: (image, kernel_size, sigmaX)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Display the blurred image
    cv2.imshow('Blurred Image', blurred_image)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
