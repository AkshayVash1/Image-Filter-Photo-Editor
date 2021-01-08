#Milestone 3 P8
#Group 69
#Group Leader: Akshay Vanishit
#Group members: Mark Zachkewich, Jose Urieta, Cameron Legree
#Authors: Mark Zachkewich, Cameron Legree
#Date of Submission: April 3rd, 2020

from Cimpl import *
from T69_user_interface import *


def batch_test_input(filename: str) -> list:
    """Returns a list where all the indices are lists containing each word in 
    filename as a string. filename must be the name of a .txt file in the same 
    folder as this .py file. It opens the file, and unpacks each line 
    contained within.
    >>>batch_test_input(batch_sample.txt)
    [['miss_sullivan.jpg','test1.jpg', '2', 'X', 'P'], 
    ['miss_sullivan.jpg','test2.jpg', 'V', 'H']]
    """ 
    infile = open(filename, 'r')
    master_lst = []
    for line in infile:
        data = line.split()
        single_test_lst = []
        for item in data:
            single_test_lst.append(item)
        master_lst.append(single_test_lst)
    infile.close
    return master_lst
    
    
filename = choose_file()
all_tests_lst = batch_test_input(filename)

for test_case in all_tests_lst:
    image_name = test_case[0]
    new_name = test_case[1]
    test_case.remove(image_name)
    test_case.remove(new_name)    
    original_image = load_image(image_name)
    
    for filter_code in test_case:
        filter_function = function_selector(filter_code)
        
        if filter_function == detect_edges or filter_function\
        == detect_edges_better: 
            threshold = 10
            new_image = apply_filter(original_image, filter_function, threshold)
            original_image = new_image
        else:
            threshold = None
            new_image = apply_filter(original_image, filter_function, threshold)
            original_image = new_image
            
    save_as(original_image, new_name)    