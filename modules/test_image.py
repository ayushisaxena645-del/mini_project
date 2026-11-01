
from modules.image_analysis import analyze_image

image_path = "sample.png"

result = analyze_image(image_path)

print("Image Analysis Result:")

if result["success"]:
    print(result["message"])
    print("Extracted Text:")
    print(result["extracted_text"])
else:
    print(result["message"])
