###############################################################################
# This programm is built to draw a white circle on a 501x501 pixels image with PIL and save it as a PNG file.
###############################################################################

# Import PIL
# Import math also
from PIL import Image # PIL is the Python Imaging Library in which Image is used to create the image and draw on the image
from math import pi, sin, cos # math is the math library in which pi and sin and cos are used to control the step and calculate the coordinate of the points of the circle with the help of the trigonometric circle and asscociated functions

# Create an Image object
img = Image.new('RGB', (501, 501), 'black') # Image of 501x501 pixels with black background in RGB mode

# Draw a circle with PIL
center = 251 # Center of the image and the circle
multiplier = 43 # Radius of the circle
size = 1 # Size corresponding to 4 or 9 pixels border

i = -pi # Start i (the step) at -pi
while i <= pi:
    # Calculate x and y coordinates
    x = center + multiplier * cos(i)
    y = center + multiplier * sin(i)
    # Put pixels on the image considering size
    img.putpixel((int(x), int(y)), (255, 255, 255))
    img.putpixel((int(x)+1, int(y)), (255, 255, 255))
    img.putpixel((int(x), int(y)+1), (255, 255, 255))
    img.putpixel((int(x)+1, int(y)+1), (255, 255, 255))
    if size != 1:
        img.putpixel((int(x)-1, int(y)), (255, 255, 255))
        img.putpixel((int(x)-1, int(y)+1), (255, 255, 255))
        img.putpixel((int(x), int(y)-1), (255, 255, 255))
        img.putpixel((int(x)+1, int(y)-1), (255, 255, 255))
        img.putpixel((int(x)-1, int(y)-1), (255, 255, 255))
    # Increment i (the step)
    i += (1/pi)/(4*pi)

# Save the image
name = 'circle_light' # The name of the image
img.save(f'{name}.png') # Save the image as a PNG file with name taken as parameter
