To handle multiple images in your code, you'll need to modify the logic to process each image individually. Below is an example of how you can adapt the code for multiple images. This example assumes you're working with a list of image paths or file names.

### Example for Multiple Images

```python
import cv2
import numpy as np

def process_images(image_paths):
    results = []
    for image_path in image_paths:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image {image_path}")
            continue

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Edge detection (Canny)
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours on the original image
        result_image = image.copy()
        cv2.drawContours(result_image, contours, -1, (0, 255, 0), 2)

        # Save or display the result
        output_path = f"processed_{image_path}"
        cv2.imwrite(output_path, result_image)
        print(f"Processed image saved to {output_path}")

        results.append(result_image)

    return results

# Example usage
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]  # Replace with your image paths
processed_images = process_images(image_paths)
```

### Key Changes:
1. **Loop through multiple images**: The function `process_images` takes a list of image paths and processes each one.
2. **Error handling**: Checks if an image was successfully loaded.
3. **Output**: Saves each processed image with a modified name (e.g., `processed_image1.jpg`).

### Customization:
- Replace `image_paths` with your actual list of image paths.
- Adjust the processing steps (e.g., blur parameters, Canny thresholds) as needed.
- If you're working with a directory of images, you can use `os.listdir()` or `glob` to get all image files.

### For Batch Processing:
If you have many images in a directory, you can use `glob` to get all image files:

```python
import glob

# Get all JPG and PNG images in a directory
image_paths = glob.glob("path/to/images/*.jpg") + glob.glob("path/to/images/*.png")
processed_images = process_images(image_paths)
```