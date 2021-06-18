from PIL import Image, ImageOps
from numpy import asarray

def find_closest_palette_color(old_pixel):
    return round(old_pixel/255) * 255

def apply_dithering(img):
    new_img = ImageOps.grayscale(img)
    grayscale_data = asarray(new_img).copy()

    rows = len(grayscale_data)
    cols = len(grayscale_data[0])

    for x in range(rows-1):
        for y in range(cols-1):
            old_pixel = grayscale_data[x][y]
            new_pixel = find_closest_palette_color(old_pixel)
            grayscale_data[x][y] = new_pixel
            error = old_pixel - new_pixel
            grayscale_data[x+1][y] += error * (7/16.0)
            grayscale_data[x+1][y-1] += error * (3/16.0)
            grayscale_data[x][y+1] += error * (5/16.0)
            grayscale_data[x+1][y+1] += error * (1/16.0)
    
    new_img = Image.fromarray(grayscale_data)
    return new_img
           
img = Image.open('frog.jpg')
img = apply_dithering(img)
img.save('frog-after.jpg')

