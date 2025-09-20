import cv2
import os

def process_images(image_paths):
    for image_path in image_paths:
        # Read the image
        image = cv2.imread(image_path)

        if image is None:
            print(f"Could not read image: {image_path}")
            continue

        # Process the image (example: convert to grayscale)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Save or display the processed image
        output_path = os.path.splitext(image_path)[0] + "_processed.jpg"
        cv2.imwrite(output_path, gray_image)
        print(f"Processed and saved: {output_path}")

# Example usage
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]  # List of image paths
process_images(image_paths)
