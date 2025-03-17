
import os
from PIL import ImageFont
font = ImageFont.load_default()

FONT_PATH = "font.ttf"
if os.path.exists(FONT_PATH):
    print("Font found!")
else:
    print("Font not found. Please check the path.")
    
    