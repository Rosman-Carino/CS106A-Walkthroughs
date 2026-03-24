# Solution With Additional For Loop
def make_up2(filename):
    image = SimpleImage(filename)
    # Code for up1 provided
    out = SimpleImage.blank(image.width + 100, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_out = out.get_pixel(x + 50, image.height - 1 - y)
            pixel_out.red = pixel.red
            pixel_out.green = pixel.green
            pixel_out.blue = pixel.blue
    
    # Setting the color to be Purple on the Left and Right Side
    for y in range(image.height):
        for x in range(50):
            left_side_pixel = out.get_pixel(x, y)
            right_side_pixel = out.get_pixel(image.width + 50 + x, y)
            left_side_pixel.green = 0
            right_side_pixel.green = 0

    return out

#Optional: Solution Without Additional Double Loop 
def make_up2(filename):
    image = SimpleImage(filename)
    # Code for up1 provided
    out = SimpleImage.blank(image.width + 100, image.height)
    for y in range(image.height):
        for x in range(image.width):
            if x < 50:
                left_side_pixel = out.get_pixel(x, y)
                right_side_pixel = out.get_pixel(image.width + 50 + x, y)
                left_side_pixel.green = 0
                right_side_pixel.green = 0
            pixel = image.get_pixel(x, y)
            pixel_out = out.get_pixel(x + 50, image.height - 1 - y)
            pixel_out.red = pixel.red
            pixel_out.green = pixel.green
            pixel_out.blue = pixel.blue
    return out
