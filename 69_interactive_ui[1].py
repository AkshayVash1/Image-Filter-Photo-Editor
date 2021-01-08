#Milestone 3 P8
#Group 69
#Group Leader: Akshay Vanishit
#Group members: Mark Zachkewich, Jose Urieta, Cameron Legree
#Authors: Mark Zachkewich, Cameron Legree
#Date of Submission: April 3rd, 2020

from Cimpl import *
from T69_user_interface import *

def arguments_user_interface() -> tuple:
    """Returns the function required to perform the users desired aaction and if
    nessary the threshold value to do so. The function prints the user interface
    and then prompts the user to input their desired action. These inputs are 
    all single charachter codes that correspond to the charcter before the 
    parentheses of each action, upper or lowercase. If the characters E,e,I,i 
    are enter the user will then be promted for a threshold value, any integer 
    value, all other senarios the threshold value will be set to None. Reulting 
    in (function_name, threshold being returned) If Q or q is inputed by the 
    user (False, None) will be returned. If an invalid input is entered, the 
    function returns ("No such command", None).
    >>>arguments_user_interface()
    L)oad image  S)ave-as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit


    : l
    (load_image, None)
    >>>arguments_user_interface()
    L)oad image  S)ave-as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit


    : X
    (extreme_contrast, None)
    >>>arguments_user_interface()
    L)oad image  S)ave-as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit


    : Q
    (None, None)
    >>>arguments_user_interface()
    L)oad image  S)ave-as
    2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize
    E)dge detect  I)mproved edge detect  V)ertical flip  H)orizontal flip
    Q)uit


    : e
    Please input your desired threshold value. 10
    (edge_detect, 10)
    """   
    print("L)oad image  S)ave-as")
    print("2)-tone  3)-tone  X)treme contrast  T)int sepia  P)osterize")
    print("E)dge detect  I)mproved edge detect  V)ertical flip  "
    "H)orizontal flip")
    print("Q)uit")
    print("\n")
    function_code = str(input(": "))
    function = function_selector(function_code)
    
    if function == detect_edges or function == detect_edges_better:
        threshold = input("Please input your desired threshold value.")
        threshold = int(threshold)
    elif function == None:
        function = "No such command."
        threshold = None
    else:
        threshold = None
        
    arguments = (function, threshold)
    return arguments


def save(image: Image, filename: str) -> None:
    """Saves the desired image in the same folder as the program as a .png file.
    """
    filename = filename + ".png"
    save_as(new_image, filename)
    
     
original_image = None
new_image = None
proceed = True

while proceed == True:
    argument = arguments_user_interface()
    function, threshold = argument
    function_type = type(function)
    
    if function == load_image:
        filename = choose_file()
        original_image = load_image(filename)
        show(original_image)
        
    elif function == False:
        proceed = False
        
    elif function_type == str:
        print(function)
        print("\n")
        
    elif original_image == None:
        print("No image loaded.")
        print("\n")  
        
    elif function == save_as:
        name = input("Please input the desired name of your new image.")
        save(new_image, name)   
        
    else:
       new_image = apply_filter(original_image, function, threshold)
       show(new_image)
       original_image = new_image