#Milestone 3 P8
#Group 69
#Group Leader: Akshay Vanishit
#Group members: Mark Zachkewich, Jose Urieta, Cameron Legree
#Authors: Mark Zachkewich, Cameron Legree, Jose Urieta, Akshay Vanishit
#Date of Submission: April 3rd, 2020

from Cimpl import *
from simple_Cimpl_filters import grayscale


def red_channel(original: Image) -> Image:
    """Written by: Jose Urieta
    Student Number: 101122928
    Returns a copy of the desired image displaying only the red channel of 
    each pixel. The parameter orginal_image must be loaded pirior to passing it 
    through the function.
    >>>red_channel(p2-orginal.jpg) #Already loaded
    Returns red_image.png
    """

    NEW_G = 0
    NEW_B = 0
    new_image = copy(original)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        new_color = create_color(r, NEW_G, NEW_B)
        set_color(new_image, x, y, new_color)
    return new_image


def green_channel(original: Image) -> Image:
    """ Written by: Cameron Legree
    Student No. 101153496
    Returns a copy of an image displaying only the green channel of each pixel.
    orginal_image must loaded pirior to passing it through the function.
    >>>green_channel(miss.sullivan.png) #Image alresady loaded
    green_image.pgn
    """

    NEW_R = 0
    NEW_B = 0
    new_image = copy(original)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        new_color = create_color(NEW_R, g, NEW_B)
        set_color(new_image, x, y, new_color)
    return new_image


def blue_channel(orginal: Image) -> Image:
    """ Written by: Mark Zachkewich
    Student #: 101159738
    Returns a copy of the desired image displaying only the blue channel of 
    each pixel. The parameter orginal_image must be loaded prior to passing it 
    through the function.
    >>>blue_channel(p2-orginal.jpg) #Already loaded
    Will return the blue_image.png
    """

    NEW_R = 0
    NEW_G = 0
    new_image = copy(orginal)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        new_color = create_color(NEW_R, NEW_G, b)
        set_color(new_image, x, y, new_color)
    return new_image


def combine(red: Image, green: Image, blue: Image) -> Image:
    """
    Written by: Akshay Vashisht
    Student Number: 101147822
    Returns an image displaying each pixels red, green, and blue channels. 
    red_image is an image that is diplaying only the red channel of each pixel. 
    green_image is an image that is diplaying only the green channel of each
    pixel. blue_image is an image that is diplaying only the blue channel of 
    each pixel. Each of the images being passed through the function must be 
    loaded prior to doing so.
    >>> combine(red_image.png, green_image.png, blue_image.png) #Already loaded
    Will return an image indentical to p2-orginal.jpeg
    """

    new_image = copy(red)
    for x, y, (r, g, b) in new_image:
        r1, g1, b = get_color(green, x, y)
        r2, g, b1 = get_color(blue, x, y)
        combined_color = create_color(r, g1, b1)
        set_color(new_image, x, y, combined_color)
    
    return new_image


def two_tone(original: Image, dark_color: str, bright_color: str) -> Image:
    """
    Written by: Mark Zachkewich
    Student No. 101159738
    Returns a copy of an image with the tree tone filter applied to it. The 
    image must be loaded pirior to passing it through the function as 
    orginal_image. For dark_color and bright_color the acceptable arguments for 
    these parmeters are: "black", "white", "red", "lime", "blue", "yellow",
    "cyan", "magenta", and "grey". dark_color will be the color that all pixels 
    with a brightness less than 128 assume. bright_color will be the color that 
    all pixels with a brightness between 128 and 255 inclusive will assume.
    >>>two_tone(miss_sullivan.png, "black", "white")
    Returns miss_sullivan.png with the two tone filter apllied where the two 
    colors are "black" and "white".
    >>>two_tone(miss_sullivan.png, "lime", "red")
    Returns miss_sullivan.png with the two tone filter apllied where the two 
    colors are "lime" and "red".
    >>>two_tone(miss_sullivan.png, "blue", "yellow")
    Returns miss_sullivan.png with the two tone filter apllied where the two 
    colors are "blue" and "yellow".
    >>>two_tone(miss_sullivan.png, "cyan", "magenta")
    Returns miss_sullivan.png with the two tone filter apllied where the two 
    colors are "cyan" and "magenta".
    >>>two_tone(miss_sullivan.png, "gray", "blue")
    Returns miss_sullivan.png with the two tone filter apllied where the two 
    colors are "gray" and "blue".
    """
    # Defines the r,g,b values for the supported arguments for dark_color and
    # light_color
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    LIME = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    GRAY = (128, 128, 128)

    # Sets the value that separates the pixels from being assigned dark_color and
    # light_color
    BOUNDARY_VALUE = 128

    dark_filter_color = dark_color
    bright_filter_color = bright_color

    # Determines which color is applied to pixels that have a brightness less
    # than BOUNDARY_VALUE.
    if dark_color == "black":
        dark_filter_color = BLACK
    elif dark_color == "white":
        dark_filter_color = WHITE
    elif dark_color == "red":
        dark_filter_color = RED
    elif dark_color == "lime":
        dark_filter_color = LIME
    elif dark_color == "blue":
        dark_filter_color = BLUE
    elif dark_color == "yellow":
        dark_filter_color = YELLOW
    elif dark_color == "cyan":
        dark_filter_color = CYAN
    elif dark_color == "magenta":
        dark_filter_color = MAGENTA
    elif dark_color == "gray":
        dark_filter_color = GRAY

    # Determines which color is applied to pixels that have a brightness greater
    # than or equal to BOUNDARY_VALUE.

    if bright_color == "black":
        bright_filter_color = BLACK
    elif bright_color == "white":
        bright_filter_color = WHITE
    elif bright_color == "red":
        bright_filter_color = RED
    elif bright_color == "lime":
        bright_filter_color = LIME
    elif bright_color == "blue":
        bright_filter_color = BLUE
    elif bright_color == "yellow":
        bright_filter_color = YELLOW
    elif bright_color == "cyan":
        bright_filter_color = CYAN
    elif bright_color == "magenta":
        bright_filter_color = MAGENTA
    elif bright_color == "gray":
        bright_filter_color = GRAY

    r_dark, g_dark, b_dark = dark_filter_color
    r_bright, g_bright, b_bright = bright_filter_color

    new_image = copy(original)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        brightness = (r + g + b) // 3
        brightness = round(brightness)
        if brightness < BOUNDARY_VALUE:
            new_color = create_color(r_dark, g_dark, b_dark)
            set_color(new_image, x, y, new_color)
        else:
            new_color = create_color(r_bright, g_bright, b_bright)
            set_color(new_image, x, y, new_color)
    return new_image


def three_tone(original: Image, dark_color: str,
               middle_color: str, bright_color: str) -> Image:
    """
    Written by: Mark Zachkewich
    Student No. 101159738
    Returns a copy of an image with the tree tone filter applied to it. The 
    image must be loaded pirior to passing it through the function as 
    orginal_image. For dark_color, middle_color, and bright_color the 
    acceptable arguments for there parmeters are: "black", "white", "red", 
    "lime", "blue", "yellow", "cyan" "magenta", and "grey". dark_color will be 
    the color that all pixels with a brightness less than 85 assume. 
    middle_color will be the color that all pixels with a brightness between 85
    and 170 inclusive will assume. bright_color will be the color that all 
    pixels with a brightness between 171 and 255 inclusive will assume. 
    >>>three_tone(miss_sullivan.png, "black", "white", "red")
    Returns miss_sullivan.png with the three tone filter apllied where the 
    colors are black, white, and red.
    >>>three_tone(miss_sullivan.png, "lime", "blue", "yellow")
    Returns miss_sullivan.png with the three tone filter apllied where the 
    colors are lime, blue, and yellow.
    >>>three_tone(miss_sullivan.png, "cyan", "magenta", "gray")
    Returns miss_sullivan.png with the two tone filter apllied where the
    colors are cyan, magenta, and gray.
    """
    # Defines each of the possible colors r,g,b values.
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    LIME = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    GRAY = (128, 128, 128)

    # Defines the brightness that is used to determine which color will be
    # applied to eah pixel
    LOWER_LIMIT = 85
    UPPER_LIMIT = 171

    dark_filter_color = dark_color
    middle_filter_color = middle_color
    bright_filter_color = bright_color

    # Determines the color that is to be applied to the pixels whoose brightness
    # is less than LOWER_LIMIT.
    if dark_color == "black":
        dark_filter_color = BLACK
    elif dark_color == "white":
        dark_filter_color = WHITE
    elif dark_color == "red":
        dark_filter_color = RED
    elif dark_color == "lime":
        dark_filter_color = LIME
    elif dark_color == "blue":
        dark_filter_color = BLUE
    elif dark_color == "yellow":
        dark_filter_color = YELLOW
    elif dark_color == "cyan":
        dark_filter_color = CYAN
    elif dark_color == "magenta":
        dark_filter_color = MAGENTA
    elif dark_color == "gray":
        dark_filter_color = GRAY

    # Determines the color that is to be applied to the pixels whoose brightness
    # is between LOWER_LIMIT and UPPER_LIMIT inclusive.
    if middle_color == "black":
        middle_filter_color = BLACK
    elif middle_color == "white":
        middle_filter_color = WHITE
    elif middle_color == "red":
        middle_filter_color = RED
    elif middle_color == "lime":
        middle_filter_color = LIME
    elif middle_color == "blue":
        middle_filter_color = BLUE
    elif middle_color == "yellow":
        middle_filter_color = YELLOW
    elif middle_color == "cyan":
        middle_filter_color = CYAN
    elif middle_color == "magenta":
        middle_filter_color = MAGENTA
    elif middle_color == "gray":
        middle_filter_color = GRAY

        # Determines the color that is applied to the pixels that have a brightness
    # between 171 and 255 inclusive.
    if bright_color == "black":
        bright_filter_color = BLACK
    elif bright_color == "white":
        bright_filter_color = WHITE
    elif bright_color == "red":
        bright_filter_color = RED
    elif bright_color == "lime":
        bright_filter_color = LIME
    elif bright_color == "blue":
        bright_filter_color = BLUE
    elif bright_color == "yellow":
        bright_filter_color = YELLOW
    elif bright_color == "cyan":
        bright_filter_color = CYAN
    elif bright_color == "magenta":
        bright_filter_color = MAGENTA
    elif bright_color == "gray":
        bright_filter_color = GRAY

    r_dark, g_dark, b_dark = dark_filter_color
    r_middle, g_middle, b_middle = middle_filter_color
    r_bright, g_bright, b_bright = bright_filter_color

    new_image = copy(original)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        brightness = (r + g + b) // 3
        brightness = round(brightness)
        if brightness < LOWER_LIMIT:
            new_color = create_color(r_dark, g_dark, b_dark)
            set_color(new_image, x, y, new_color)
        elif brightness < UPPER_LIMIT:
            new_color = create_color(r_middle, g_middle, b_middle)
            set_color(new_image, x, y, new_color)
        else:
            new_color = create_color(r_bright, g_bright, b_bright)
            set_color(new_image, x, y, new_color)
    return new_image


def extreme_contrast(original: Image) -> Image:
    """Written by: Jose Urieta
    Student No. 101122928
    Returns a copy an image with the extreme contrast filter applied to it. 
    orginal_image must be loaded pirior to passing through the function.
    >>>extreme_contrast(miss_sullivan.png)
    """
    # Declares the extreme values that the dark and bright pixels will become
    # along with value that divides the light pixels and range and dark pixels
    # range.
    DARK = 0
    BRIGHT = 255
    BOUNDARY_VALUE = 127
    new_image = copy(original)

    for x, y, (r, g, b) in original:
        # Determines weather the new r,g,b values are 0 or 255 for each pixel.
        if r <= BOUNDARY_VALUE:
            new_r = DARK
        else:
            new_r = BRIGHT
        if g <= BOUNDARY_VALUE:
            new_g = DARK
        else:
            new_g = BRIGHT
        if b <= BOUNDARY_VALUE:
            new_b = DARK
        else:
            new_b = BRIGHT

        extreme_color = create_color(new_r, new_g, new_b)
        set_color(new_image, x, y, extreme_color)
    return new_image


def sepia(original: Image) -> Image:
    """Written by: Cameron Legree
    Student No. 101153496
    Returns a copy of an image that has been converted to grayscale, then tinted
    to a slight yellow colour. Pirior to passing orginial_image through the 
    function it must be loaded.
    >>>sepia(miss_sullivan.png) #image was already loaded
    returns miss_sullivan.png with the sepia filter applied.
    """
    DARK_PIXEL_LIMIT = 62
    MIDDLE_PIXEL_LIMIT = 191
    DARK_RED_MULTIPLIER = 1.1
    DARK_BLUE_MULTIPLIER = 0.9
    MIDDLE_RED_MULTIPLIER = 1.15
    MIDDLE_BLUE_MULTIPLIER = 0.85
    BRIGHT_RED_MULTIPLIER = 1.08
    BRIGHT_BLUE_MULTIPLIER = 0.93

    gray_image = grayscale(original)
    new_image = copy(gray_image)

    for pixel in gray_image:
        x, y, (r, g, b) = pixel
        if r <= DARK_PIXEL_LIMIT:
            new_r = r * DARK_RED_MULTIPLIER
            new_b = b * DARK_BLUE_MULTIPLIER
            new_color = create_color(new_r, g, new_b)
            set_color(new_image, x, y, new_color)
        elif r <= MIDDLE_PIXEL_LIMIT:
            new_r = r * MIDDLE_RED_MULTIPLIER
            new_b = b * MIDDLE_BLUE_MULTIPLIER
            new_color = create_color(new_r, g, new_b)
            set_color(new_image, x, y, new_color)
        else:
            new_r = r * BRIGHT_RED_MULTIPLIER
            new_b = b * BRIGHT_BLUE_MULTIPLIER
            new_color = create_color(new_r, g, new_b)
            set_color(new_image, x, y, new_color)
    return new_image


def _adjust_component(val: int) -> int:
    """
    Written by Akshay Vashisht
    Returns the midpoint of the quadrant in which val is in. val must be 
    between 0 and 255 inclusive. The 4 quadrants are 0 to 63, 64 to 127, 
    128 to 191, 192 to 255. The repespective midpoints of these quadrants are
    31, 95, 159, and 233.
    >>> _adjust_component(21)
    31
    >>>_adjust_component(100)
    95
    >>>_adjust_component(177)
    159
    >>>_adjust_component(222)
    223
    """
    if val <= 63:
        val = 31
    elif val <= 127:
        val = 95
    elif val <= 191:
        val = 159
    elif val <= 255:
        val = 223

    return val


def posterize(orginal: Image) -> Image:
    """
    Written by: Akshay Vashisht
     
    
    
    >>> posterize(miss.sullivan.png)
    Returns a copy of miss.sullivan.png with the postrize filter applied to it.
    """

    new_image = copy(orginal)

    for x, y, (r, g, b) in new_image:
        new_color = create_color(_adjust_component(r),
                                  _adjust_component(g),
                                  _adjust_component(b))
        set_color(new_image, x, y, new_color)

    return new_image


def detect_edges(original: Image, threshold: float) -> Image:
    """
    Written by: Akshay Vashisht
    Sets the rgb value of a pixel to either black or white depending on the 
    contrast values of those pixels. It accomplishes this by comparing the 
    pixel to the one below it. It then compares the RGB values from both 
    and takes the abosulte difference. If the difference exceeds the 
    threshold, it will turn the pixel black, otherwise it will turn white.
    >>> detect_edges(miss.sullivan.png, 50)
    """

    new_image = copy(original)

    # Defines the possible r,g,b values that pixels can be set to.
    BLACK = create_color(0, 0, 0)
    WHITE = create_color(255, 255, 255)

    for x in range(get_width(new_image)):
        for y in range(get_height(new_image)):

            if y == get_height(new_image)-1:
                set_color(new_image, x, y, WHITE)

            else:
                r, g, b = get_color(new_image, x, y)
                r1, g1, b1 = get_color(new_image, x, (y + 1))

                brightness = (r + g + b) // 3
                brightness1 = (r1 + g1 + b1) // 3

                if abs(brightness - brightness1) > threshold:

                    set_color(new_image, x, y, BLACK)

                else:
                    set_color(new_image, x, y, WHITE)

    return new_image


def detect_edges_better(original: Image, threshold: float) -> Image:
    """ 
    Written by: Jose Urieta
    
    Takes an image and a threshold value as parameters. It highlights
    edges of an image by looking at a single pixel and comparing pixels 
    to the right and below of it. It then takes the absolute difference 
    between the pixels RGB and compares its value to the threshold. If 
    the threshold is greater than the compared value, it will turn white.
    If it exceeds the threshold, it will turn black
    
    >>> detect_edges_better(miss.sullivan.png, 15)
    """
   
    BLACK = create_color(0, 0, 0)
    WHITE = create_color(255, 255, 255)

    new_image = copy(original)

    h = (get_height(new_image) - 1)
    w = (get_width(new_image) - 1)
    
    for x, y, (r, g, b) in new_image:
        
        if x == w or y == h:
            
            set_color(new_image, x, y, WHITE)

        else:
            brightness1 = (r + g + b) / 3
            r1, g1, b1 = get_color(new_image, x + 1, y)
            
            brightness2 = (r1 + g1 + b1) // 3
            
            contrast1 = brightness1 - brightness2
            r2, g2, b2 = get_color(new_image, x, y + 1)
            
            brightness3 = (r2 + g2 + b2) // 3
            
            contrast2 = brightness1 - brightness3
            
            if abs(contrast1) > threshold or abs(contrast2) > threshold:
                set_color(new_image, x, y, BLACK)
            else:
                set_color(new_image, x, y, WHITE)

    return new_image


def flip_vertical(original: Image) -> Image:
    """
    Written by: Mark Zachkewich
    Returns a copy of the desired image, flipped along a vertical line in the 
    center of the image. orginal_image must be load pirior to passing it 
    through the function.
    >>>flip_vertical(miss_sullivan.png) #loaded prior
    Returns a copy of miss_sulllivan.png flipped vertically.
    """

    new_image = copy(original)
    width = get_width(original)
    range_of_x = width - 1  # Finds the x value of the rightmost pixels.

    for pixel in original:
        x, y, (r, g, b) = pixel
        color = create_color(r, g, b)
        new_x = abs(range_of_x - x)
        set_color(new_image, new_x, y, color)
    return new_image


def flip_horizontal(original: Image) -> Image:
    """Written by: Cameron Legree
    Student No. 101153496 
    Returns a copy of an image flipped along a horiontal line centered in the 
    image. orginal_image must be loaded prior to passing it through the 
    function.
    >>>flip_horizontal(miss_sullivan.png)
    Returns a copy of miss_sullivan.png mirrored about the central horizontal 
    axis.
    """

    new_image = copy(original)
    height = get_height(original)
    range_of_y = height - 1  # Determines the y value of the bottom most pixels

    for pixel in original:
        x, y, (r, g, b) = pixel
        color = create_color(r, g, b)
        new_y = range_of_y - y
        set_color(new_image, x, new_y, color)
    return new_image



