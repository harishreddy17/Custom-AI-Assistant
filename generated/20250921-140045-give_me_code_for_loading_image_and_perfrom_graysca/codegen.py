# Loading and Converting an Image to Grayscale

Here's Python code using OpenCV and PIL (Pillow) libraries to load an image and convert it to grayscale:

## Using OpenCV

```python
import cv2

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load image")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)

    # Save the grayscale image
    cv2.imwrite('grayscale_image.jpg', gray_image)

    # Wait for a key press and then close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

## Using PIL (Pillow)

```python
from PIL import Image

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with your image path
try:
    image = Image.open(image_path)

    # Convert to grayscale
    gray_image = image.convert('L')

    # Display the images
    image.show(title='Original Image')
    gray_image.show(title='Grayscale Image')

    # Save the grayscale image
    gray_image.save('grayscale_image_pillow.jpg')

except FileNotFoundError:
    print("Error: Could not find the image file")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Using Matplotlib (for display)

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load the image
image_path = 'path_to_your_image.jpg'  # Replace with your image path
try:
    image = mpimg.imread(image_path)

    # Convert to grayscale (using luminance calculation)
    if len(image.shape) == 3:  # Check if image is color
        gray_image = 0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2]
    else:
        gray_image = image  # Already grayscale

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

    # Save the grayscale image
    plt.imsave('grayscale_image_matplotlib.jpg', gray_image, cmap='gray')

except FileNotFoundError:
    print("Error: Could not find the image file")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Notes:
1. Make sure you have the required libraries installed:
   - For OpenCV: `pip install opencv-python`
   - For PIL: `pip install pillow`
   - For Matplotlib: `pip install matplotlib`

2. Replace `'path_to_your_image.jpg'` with the actual path to your image file.

3. The grayscale conversion methods differ slightly between libraries:
   - OpenCV uses a specific color conversion code
   - PIL uses the 'L' mode which converts to luminance
   - Matplotlib uses a weighted sum of RGB channels

Choose the method that best fits your needs and existing project setup.