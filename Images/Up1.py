def make_up1(filename):
    image = SimpleImage(filename)
    output_image = SimpleImage.blank(image.width + 100,
                                image.height)
    # Iterate through the Original Image
    for y in range(image.height):
        for x in range(image.width):
           pixel_input = image.get_pixel(x,y)
           pixel_output = output_image.get_pixel(
               x + 50, image.height - 1 - y)
           pixel_output.red = pixel_input.red
           pixel_output.green = pixel_input.green
           pixel_output.blue = pixel_input.blue
    return output_image
