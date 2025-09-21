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
