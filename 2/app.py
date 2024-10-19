import cv2
import numpy as np

# Function to filter specific color range
def filter_color(image, lower_color, upper_color):
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv_image, lower_color, upper_color)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    return result

def main():
    # Load the image
    image_path = '/Users/alex/Desktop/workspace/Python/opencv/open-cv-projects/1/Human_faces.jpg'  # Replace with your image path
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not read the image.")
        return

    # Define the color range for filtering (example: red color in HSV)
    lower_red = np.array([0, 120, 70])  # Lower boundary of the color
    upper_red = np.array([10, 255, 255])  # Upper boundary of the color

    # Apply the color filter
    filtered_image = filter_color(image, lower_red, upper_red)

    # Display the original and filtered images
    cv2.imshow("Original Image", image)
    cv2.imshow("Filtered Image", filtered_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
