# Loading and Saving Images using OpenCV

Here's a simple Python code example using OpenCV to load an image from a file and save it to a different file:

```python
import cv2

def load_and_save_image(input_path, output_path):
    """
    Load an image from input_path and save it to output_path using OpenCV.

    Parameters:
    - input_path: str, path to the input image file
    - output_path: str, path to save the output image file
    """
    try:
        # Read the image
        image = cv2.imread(input_path)

        if image is None:
            print(f"Error: Could not load image from {input_path}")
            return

        # Display the image (optional)
        cv2.imshow('Original Image', image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()

        # Save the image
        cv2.imwrite(output_path, image)
        print(f"Image successfully saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = "input.jpg"  # Replace with your input image path
    output_image_path = "output.png"  # Replace with your desired output path

    load_and_save_image(input_image_path, output_image_path)
```

## Notes:

1. **Image Formats**: OpenCV supports common image formats like JPEG, PNG, BMP, etc. The output format is determined by the file extension you use.

2. **Color Handling**:
   - By default, `cv2.imread()` loads images in BGR color format (OpenCV's default)
   - If you need RGB format, you can convert it with: `image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)`

3. **Error Handling**: The code includes basic error handling for cases where the image can't be loaded.

4. **Installation**: Make sure you have OpenCV installed. You can install it with:
   ```
   pip install opencv-python
   ```

5. **Displaying Images**: The example includes code to display the image, but you can remove this if you only want to process and save images.

Would you like me to modify this example for any specific use case?