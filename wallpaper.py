from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Settings
WIDTH, HEIGHT = 3840, 2160  # Wallpaper resolution
BACKGROUND_COLOR = (0, 0, 0)  # Black
BINARY_COLOR = (0, 255, 0) # Green
FONT_SIZE = 20
FONT_PATH = "./Courier_Prime/CourierPrime-Regular.ttf"  
BINARY_TEXT = "0101010101010101" * 1000  

# Create a black background
image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

# Load the image (non-black-and-white)
input_image = Image.open("newer.png").convert("L")  
input_image = input_image.resize((WIDTH, HEIGHT))  \
    
# Convert image to numpy array
image_array = np.array(input_image)

# Overlay binary text based on grayscale intensity
x, y = 0, 0
binary_index = 0
while y < HEIGHT:
    while x < WIDTH:
        # Use grayscale intensity to determine if binary text should be placed
        intensity = image_array[y, x]
        if intensity < 215:  # Adjust this threshold to control text density
            # Draw binary text
            draw.text((x, y), BINARY_TEXT[binary_index % len(BINARY_TEXT)], font=font, fill=BINARY_COLOR)
            binary_index += 1
        x += FONT_SIZE  # Move to the next position
    x = 0
    y += FONT_SIZE  # Move to the next line

# Save the wallpaper
image.save("binary_hands_wallpaper_day.png")
print("Wallpaper saved as 'binary_hands_wallpaper_day.png'")