import cv2

# Load an image from file
image_path = 'path/to/your/image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image from {image_path}")
else:
    # Display the image
    cv2.imshow('Loaded Image', image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the image (optional)
    # cv2.imwrite('output_image.jpg', image)
