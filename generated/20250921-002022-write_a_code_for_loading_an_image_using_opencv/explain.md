# Loading an Image Using OpenCV

Here's a simple Python code snippet to load an image using OpenCV (cv2):

```python
import cv2

def load_image(image_path):
    """
    Load an image from the specified path using OpenCV.

    Parameters:
    image_path (str): Path to the image file

    Returns:
    numpy.ndarray: The loaded image as a NumPy array
    """
    # Read the image in color (BGR format by default)
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return None

    print(f"Image loaded successfully. Shape: {image.shape}")
    return image

# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "example.jpg"

    # Load the image
    img = load_image(image_path)

    if img is not None:
        # Display the image (optional)
        cv2.imshow("Loaded Image", img)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()
```

## Notes:

1. Make sure you have OpenCV installed. You can install it with:
   ```
   pip install opencv-python
   ```

2. The `imread` function returns a NumPy array representing the image in BGR format (by default).

3. Common image formats supported include: JPEG, PNG, BMP, etc.

4. If you want to load the image in grayscale, use:
   ```python
   image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
   ```

5. For images with transparency (PNG with alpha channel), you might need to handle them differently.

6. The image shape will be (height, width, channels) where channels is 3 for color images and 1 for grayscale.