import cv2

# Load an image from file
image_path = 'path_to_your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    print(f"Image loaded successfully. Dimensions: {image.shape}")

    # Display the image
    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()
