# Loading and Saving Images with OpenCV

Here's a simple Python code example using OpenCV to load an image from a file and save it to another file:

```python
import cv2

def load_and_save_image(input_path, output_path):
    """
    Load an image from input_path and save it to output_path.

    Args:
        input_path (str): Path to the input image file
        output_path (str): Path where the output image will be saved
    """
    try:
        # Load the image
        image = cv2.imread(input_path)

        # Check if the image was loaded successfully
        if image is None:
            print(f"Error: Could not load image from {input_path}")
            return

        # Save the image
        cv2.imwrite(output_path, image)
        print(f"Image successfully saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image_path = "input.jpg"  # Replace with your input image path
    output_image_path = "output.jpg"  # Replace with your desired output path

    load_and_save_image(input_image_path, output_image_path)
```

## Additional Notes:

1. **Image Formats**: OpenCV can read and write many common image formats including:
   - JPEG (`.jpg`, `.jpeg`)
   - PNG (`.png`)
   - BMP (`.bmp`)
   - TIFF (`.tiff`, `.tif`)

2. **Color vs Grayscale**:
   - By default, `cv2.imread()` loads images in BGR color format
   - To load as grayscale: `cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)`
   - To save as grayscale: `cv2.imwrite(output_path, grayscale_image)`

3. **Error Handling**: The code includes basic error handling for:
   - File not found
   - Invalid image format
   - Permission issues

4. **Installation**: If you don't have OpenCV installed, you can install it with:
   ```
   pip install opencv-python
   ```

Would you like me to modify this example for any specific use case or add any additional functionality?