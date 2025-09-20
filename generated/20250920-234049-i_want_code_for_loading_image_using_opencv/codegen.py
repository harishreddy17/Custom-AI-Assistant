# Loading an Image Using OpenCV in Python

Here's a simple code example to load an image using OpenCV (cv2) in Python:

```python
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
```

## Additional Options:

1. **Loading in grayscale**:
```python
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
```

2. **Loading with alpha channel (for PNG images)**:
```python
rgba_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
```

3. **Checking image properties**:
```python
if image is not None:
    print(f"Image shape: {image.shape}")  # (height, width, channels)
    print(f"Image type: {image.dtype}")   # Typically uint8
```

## Requirements:
- You need to have OpenCV installed. If you don't have it, install it with:
  ```
  pip install opencv-python
  ```