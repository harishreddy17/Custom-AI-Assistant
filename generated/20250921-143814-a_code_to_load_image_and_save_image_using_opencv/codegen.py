# Loading and Saving Images using OpenCV in Python

Here's a simple Python script that demonstrates how to load an image and save it using OpenCV:

```python
import cv2

def load_and_save_image(input_path, output_path):
    """
    Load an image from file and save it to another location.

    Args:
        input_path (str): Path to the input image file
        output_path (str): Path where the output image will be saved
    """
    try:
        # Load the image
        image = cv2.imread(input_path)

        if image is None:
            print(f"Error: Could not load image from {input_path}")
            return

        # Display the image (optional)
        cv2.imshow('Loaded Image', image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()

        # Save the image
        cv2.imwrite(output_path, image)
        print(f"Image successfully saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_image = "input.jpg"  # Replace with your input image path
    output_image = "output.jpg"  # Replace with your desired output path

    load_and_save_image(input_image, output_image)
```

## Notes:

1. **Image Formats**: OpenCV can read and write many image formats including JPEG, PNG, BMP, etc.

2. **Color Handling**:
   - By default, `cv2.imread()` loads images in BGR format (not RGB)
   - If you need RGB format, you can convert it with: `cv2.cvtColor(image, cv2.COLOR_BGR2RGB)`

3. **Error Handling**: The code includes basic error handling for cases where the image can't be loaded.

4. **Dependencies**: You'll need to have OpenCV installed. If you don't have it, install it with:
   ```
   pip install opencv-python
   ```

5. **Displaying Images**: The code includes optional image display functionality. Remove the `cv2.imshow()` and related lines if you don't need to display the image.

Would you like me to modify this code for any specific requirements?