# Loading an Image Using OpenCV

Here's a simple Python code example to load an image using OpenCV (cv2):

```python
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
```

## Additional Options:

1. **Loading in grayscale**:
```python
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
```

2. **Loading with alpha channel (if image has transparency)**:
```python
rgba_image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
```

3. **Saving the loaded image**:
```python
cv2.imwrite('output_image.jpg', image)
```

## Notes:
- Make sure you have OpenCV installed (`pip install opencv-python`)
- The image path should be either absolute or relative to your working directory
- The `cv2.imshow()` function will display the image in a window that closes when you press any key
- The image shape is returned as (height, width, channels) in BGR format by default