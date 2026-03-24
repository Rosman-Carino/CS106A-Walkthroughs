def aqua_bars(filename, bar_height):
    image = SimpleImage(filename)
    out = SimpleImage.blank(image.width, image.height + (2 * bar_height))
    # Step 1: Copy the Original Image to the Output Image
    for y in range(image.height):
        for x in range(image.width):
            input_pixel = image.get_pixel(x, y)
            out_pixel = out.get_pixel(x, y + bar_height)
            out_pixel.red = input_pixel.red
            out_pixel.green = input_pixel.green
            out_pixel.blue = input_pixel.blue
    # Step 2: Setting up the Colors for the Bars
    for y in range(bar_height):
        for x in range(image.width):
            top_pixel = out.get_pixel(x, y)
            top_pixel.red = 0
            bottom_pixel = out.get_pixel(x, image.height + bar_height + y)
            bottom_pixel.red = 0
    return out
