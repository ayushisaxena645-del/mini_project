
import cv2
import pytesseract
import os

# If Tesseract is not automatically detected on Windows,
# uncomment this line and update the path if necessary.
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# )


def analyze_image(image_path):

    # Check whether image exists
    if not os.path.exists(image_path):
        return {
            "success": False,
            "message": "Image file not found"
        }

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        return {
            "success": False,
            "message": "Unable to read image"
        }

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(gray)

    # Return analysis result
    return {
        "success": True,
        "message": "Image analysis completed",
        "extracted_text": extracted_text.strip()
    }
