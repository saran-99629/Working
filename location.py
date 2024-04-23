import pyautogui 

loc = pyautogui.locateOnScreen('loc.png')

print(loc)

import pyautogui
import pytesseract
# Define the coordinates of the region you want to capture
left = 70
top = 40
width = 800
height = 70

# Capture the screenshot of the defined region
screenshot = pyautogui.screenshot(region=(left, top, width, height))

# Save the screenshot to a file
screenshot.save("out.png")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

from PIL import Image

# Open the image containing text
test_image = Image.open("loc.png")

# Perform OCR using pytesseract
text = pytesseract.image_to_string(test_image)

# Print the extracted text
print("Extracted Text:")
print(text)