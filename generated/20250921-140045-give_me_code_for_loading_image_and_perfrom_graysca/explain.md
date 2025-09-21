# Loading and Converting an Image to Grayscale

Here's Python code using OpenCV and PIL libraries to load an image and convert it to grayscale:

## Using OpenCV (cv2)

```python
import cv2

# Load the image
image = cv2.imread('input_image.jpg')  # Replace with your image path

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('output_grayscale.jpg', gray_image)

# Display the images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)  # Wait for a key press to close windows
cv2.destroyAllWindows()
```

## Using PIL (Python Imaging Library)

```python
from PIL import Image

# Load the image
image = Image.open('input_image.jpg')  # Replace with your image path

# Convert to grayscale
gray_image = image.convert('L')

# Save the grayscale image
gray_image.save('output_grayscale.jpg')

# Display the images (optional)
image.show()
gray_image.show()
```

## Using Matplotlib (for display only)

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image = mpimg.imread('input_image.jpg')

# Convert to grayscale (using luminance formula)
gray_image = image.dot([0.2989, 0.5870, 0.1140]) if image.ndim == 3 else image

# Display the images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.show()
```

### Notes:
1. Make sure you have the required libraries installed:
   - `pip install opencv-python` for OpenCV
   - `pip install pillow` for PIL
   - `pip install matplotlib` for Matplotlib

2. Replace 'input_image.jpg' with the path to your image file.

3. The grayscale conversion methods are slightly different:
   - OpenCV uses a specific color space conversion
   - PIL uses a standard luminance formula
   - Matplotlib uses a custom dot product with weights

Choose the method that best fits your needs!