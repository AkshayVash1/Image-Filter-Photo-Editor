#Milestone 3 P8
#Group 69
#Group Leader: Akshay Vanishit
#Group members: Mark Zachkewich, Jose Urieta, Cameron Legree
#Authors: Mark Zachkewich
#Date of Submission: April 3rd, 2020

from Cimpl import *
from T69_image_filters import *


def apply_filter(original_image: Image, filter_name, threshold: int) -> Image:
    """Returns orginal image with the desired filter, filter_name, appied to it. 
    thershold is only only assigned a value if the arguemnt for filter_name is 
    detect_edges or detect_edges_better. If the argument for filter name is 
    two_tone the bright pixels will become cyan while the drak pixels will
    become yellow. If the argument for filter name is three_tone the bright 
    pixels will become cyan, the dark pixels will become yellow, and the middle 
    ranged pixels will become magenta.
    >>>apply_filter(miss_sullivan.png, two_tone, none)
    returns a copy of miss_sullivan.png with the two tone filter applied
    
    >>>apply_filter(miss_sullivan.png, three_tone, none)
    returns a copy of miss_sullivan.png with the three tone filter applied
    
    >>>apply_filter(miss_sullivan.png, extreme_contrast, none)
    returns a copy of miss_sullivan.png with the extreme contrast filter applied
    
    >>>apply_filter(miss_sullivan.png, sepia, none)
    returns a copy of miss_sullivan.png with the sepia filter applied
    
    >>>apply_filter(miss_sullivan.png, posterize, none)
    returns a copy of miss_sullivan.png with the posterizing filter applied
    
    >>>apply_filter(miss_sullivan.png, detect_edges, 10)
    returns a copy of miss_sullivan.png with the detect edges filter with a 
    threshold of 10 applied
    
    >>>apply_filter(miss_sullivan.png, detect_edges_better, 12)
    returns a copy of miss_sullivan.png with the detect edges better filter with
    a threshold of 12 applied
    
    >>>apply_filter(miss_sullivan.png, vertical_flip, none)
    returns a copy of miss_sullivan.png with the vertical flip filter applied
    
    >>>apply_filter(miss_sullivan.png, horizontal_flip, none)
    returns a copy of miss_sullivan.png with the horizontal filter applied
    """
    
    TWO_TONE_DARK_COLOR = "yellow"
    TWO_TONE_BRIGHT_COLOR = "cyan"
    THREE_TONE_DARK_COLOR = "yellow"
    THREE_TONE_MIDDLE_COLOR = "magenta"
    THREE_TONE_BRIGHT_COLOR = "cyan"
    if threshold == None:
        if filter_name == two_tone:
            new_image = two_tone(original_image, TWO_TONE_DARK_COLOR,\
            TWO_TONE_BRIGHT_COLOR)
        elif filter_name == three_tone:
            new_image = three_tone(original_image, THREE_TONE_DARK_COLOR,\
            THREE_TONE_MIDDLE_COLOR, TWO_TONE_BRIGHT_COLOR)
        else:
            new_image = filter_name(original_image)       
    else:
        new_image = filter_name(original_image, threshold)
    return new_image


def function_selector(function_code: str):
    """Returns the function that corresponds to function_code. If function_code 
    does not correspond to a function none is returned. The values that will 
    not cause the function to return none are:  "L", "l", "S", "s", "2", "3", 
    "X", "x", "T", "t", "P", "p", "E", "e", "I", "i", "V", "v", "H", "h", "Q", 
    "q". 
    >>>_function_selector("L")
    load_image
    >>>_function_selector("l")
    load_image
    >>>_function_selector("S")
    save_as
    >>>_function_selector("s")
    save_as
    >>>_function_selector("2")
    two_tone
    >>>_function_selector("3")
    three_tone
    >>>_function_selector("X")
    extreme_contrast
    >>>_function_selector("x")
    extreme_contrast
    >>>_function_selector("T")
    sepia
    >>>_function_selector("t")
    sepia
    >>>_function_selector("P")
    posterize
    >>>_function_selector("p")
    posterize
    >>>_function_selector("E")
    detect_edges
    >>>_function_selector("e")
    detect_edges
    >>>_function_selector("I")
    detect_edges_better
    >>>_function_selector("i")
    detect_edges_better
    >>>_function_selector("V")
    flip_vertical
    >>>_function_selector("v")
    flip_vertical
    >>>_function_selector("H")
    flip_horizontal
    >>>_function_selector("h")
    flip_horizontal
    >>>_function_selector("Q")
    False
    >>>_function_selector("q")
    False
    >>>_function_selector("kk")
    None
    """
    
    operator_functions = {"L":load_image, "l":load_image, "S": save_as,\
                          "s":save_as, "2":two_tone, "3":three_tone,\
                          "X":extreme_contrast, "x":extreme_contrast,\
                          "T":sepia, "t":sepia, "P":posterize, "p":posterize,\
                          "E":detect_edges, "e":detect_edges,\
                          "I":detect_edges_better, "i":detect_edges_better,\
                          "V":flip_vertical, "v":flip_vertical, \
                          "H":flip_horizontal, "h":flip_horizontal, "Q":False,\
                          "q":False}
    len_function_code = len(function_code)
    if function_code not in operator_functions or len_function_code != 1:
        function = None
    else:
        function = operator_functions[function_code]
    return function