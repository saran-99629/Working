import pyautogui
from PIL import Image
import pytesseract

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Define the region to capture (left, top, width, height)
region = (10, 10, 1920, 700)  # Example region coordinates

# Capture the screen of the specified region
screenshot = pyautogui.screenshot(region=region)

# Save the screenshot
screenshot.save("screenshot.png")

# Open the saved screenshot image
image = Image.open("screenshot.png")

# Perform any necessary image processing (e.g., converting to grayscale)
# image = image.convert("L")  # Convert to grayscale

# Perform OCR using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)
