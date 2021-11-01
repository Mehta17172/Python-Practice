# Install PIL/Pillow library using command 'pip install Pillow' in CMD Prompt

# import Pillow
from types import ClassMethodDescriptorType
from PIL import Image

# Create object for Image csgo.png
csgo_img = Image.open('csgo.png')

# Show the image
def showImage(img):
    img.show()

# Basics in PIL/Pillow

# functions to resize the image
def resize_images( image_names, new_size = (800, 500)):
    for image_name in image_names:
        img = Image.open(image_name) # opens an image and creates an object for it
        img = img.resize(new_size) # resizes the dimensions of the image
        img.save("resized_" + image_name) # create and saves the new image

images = ["csgo.jpg","valorant.jpg","csgo.png"]
resize_images(images)

#  crop an image

csgo_img = Image.open('csgo.png')
# showImage(csgo_img)
csgo_img = csgo_img.crop((100,100,500,500)) # syntax for cropping an image: image_name.crop((x1,y1,x2,y2))
# showImage(csgo_img)

# rotate an image

csgo_img = csgo_img.rotate(90) # syntax for rotating an image: image_name.rotate(degree)
# showImage(csgo_img)

# Picture Manipulations:

from PIL import Image, ImageFilter, ImageEnhance
csgo_img = Image.open('csgo.png')

# Edge Detection

edge_detect = csgo_img.filter(ImageFilter.FIND_EDGES)
# showImage(edge_detect)

# Blur Image

blur_img = csgo_img.filter(ImageFilter.BLUR)
# showImage(blur_img)

# Grayscale

grayscale_img = csgo_img.convert("L")
# showImage(grayscale_img)

# Contrast

# showImage(csgo_img)
contrast_img = ImageEnhance.Contrast(csgo_img).enhance(3.5)
# showImage(contrast_img)

# Brightness

bright_img = ImageEnhance.Contrast(csgo_img).enhance(5)
# showImage(bright_img)

#  Negating an image

def generate_negative(img_name):
    img = Image.open(img_name)
    width, height = img.size
    for x in range(0,width):
        for y in range(0,height):
            pixel_coordinate = (x,y)
            r, g, b, alpha = img.getpixel(pixel_coordinate) # for png we need four channels, for jpg or jpeg we need only three channel
            negative_color = (255 - r,255 - g,255 - b)
            img.putpixel( pixel_coordinate, negative_color)
    return img
negative_img = generate_negative("csgo.png")
negative_img.save("Negative csgo.png") 
showImage(negative_img)


