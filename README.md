# Image-Filter-Photo-Editor

ECOR1051 Winter 2020 README for Photo Editor, Project Version 1.0, 7/4/2020

The project leader, Akshay Vashisht can be reached at:
Voice: (613)-857-8545
Email: aksahyvashist@cmail.carleton.ca
Website: https://culearn.carleton.ca/moodle/course/view.php?id=144561

Description:
____________

- This package contains two programs, one that user uses a user interface to apply the filtersand the second is a program that 
uses a .txt file when bulk image processing is required. When loaded the user interface when display all supported actions to the user
and allow them to load an image, applying 1 or more of the 8 available filters, cumulativley, before saving their new, filtered, image and existing 
the program.


- The package is comprised of 4 files:
	T69_batch_ui.py        ->        Script which uses the batch text file to filter an image
	T69_image_filters.py   ->        Script containing all image filters.
	69_user_interfaces.py  ->        Script that is used by both T69_batch_ui.py and T69_interactive_ui.py
	69_interactive_ui.py   ->        Script which asks the user to input a command or filter


Installation:
_____________

- To properly run the program, the following must be installed and configured accordingly:
	Python 3.7.4 or newer
	Pillow 7.0.0 or newer
	Cimpl.py 1.04
	simple_Cimpl_filters.py 1.0

- Python must be installed to PATH for the package to work properly and can be found at https://www.python.org/downloads/.

- Pillow is to be installed after Python and can be found at https://pypi.org/project/Pillow/.

- Cimpl.py and simple_Cimpl_filters.py are to be downloaded from the ECOR 1051 CuLearn page. This file is located under the "Milestone 1" tab 
and with in the file "P1 Task 4 - A folder containing Cimpl.py and Approved Sample Images." Once downloaded both of these python files must 
be added to the directory containing purachsed software package.


Usage:
______

- The interactive UI works in the following manner:
 	Once opened the following shell command will be displayed to the user: 
 	>>> L)oad image  S)ave-as 
	2)-tone 3)-tone X)treme contrast T)int sepia P)osterize 
	E)dge detect I)mproved edge detect V)vertical flip H)orizontal flip 
	Q)uit

	:

	Once displayed the user is required in enter "L" or "l" trying to execute anyother command, except for quit, willcause an error and 
	"No image loaded" to be displayed. After this command the user will be prompted to select any image they wish to filter that is on 
	their machine. Once an image is loaded, the program will  display the orginal image to the user and only after the user closes the 
	window displaying the orginal image will it be possible to apply filiters to the image. The following prompt then appears again
 	>>>L)oad image  S)ave-as 
	2)-tone 3)-tone X)treme contrast T)int sepia P)osterize 
	E)dge detect I)mproved edge detect V)vertical flip H)orizontal flip 
	Q)uit
	
	:
	and requires the user to input one of the signle charcter codes that repersent which filter they wish to apply to their image. The 
	code is the charcter pirior to the parentheses, this my be upper of lowercase. Once the filter is selected and applied to the image
	the reult will appear in a pop up window for the user to veiw, this window must be closed before continuing. The program applies
	allowing for the user to continue modifiying the image if the wish. Once the user is satisfied with their work they will input "s" or "S" to
	save their image doing so causes the folowing prompt to appear:
	>>>Please input the desired name of your new image.
	Once the user inputs their desired name for the new file the filtered image will be saved, as a .png, in the same directory as the 
	purachased software. The user may repeat the process to filter another image or enter "q" or "Q' to Quit the program.
	NOTE: When selecting the Edge Detecht or Improved Edge Deteccht Filters the user will be prompted to enter a threshold value,
	this can be any integer from 0 to 100. 
	>>>Please input your desired threshold value.

- The batch user interface functions in the follwoing manner:
	The program will open file explorer and prompt the user to select their desired .txt file for the batch UI to use during image processing. The 
	.txt file being used must be located in the same directory as the images being filtered. The format of this file must follow a specifed format
	as each line must contain the actions pertaining to each image. The order of the information is also important as first must be the image to be
	filitered, followed by the name at which it will be saved as once filitered, then the single character commands that represent the desired 
	filiters to be applied, these are the same as the interactive userface. Each of the different pieces of information in .txt file must be 
	separtated by a space. After selecting the image the UI will fillter the images and desired and will be saved to the same directoy as the .txt file.
	To view the filtered imag ethe user must manual open it once it has been saved.


Credits:
________

-Akshay Vashisht, 101147822 - combine, _adjust_component, posterize, detect_edges

-Mark Zachkewich, 101159738 - blue_channel, two_tone, three_tone, flip_vertical, apply_filters, function_selector, arguments_user_interface
save, batch_test_input

-Jose Urieta, 101122938 - red_channe, extreme_contrast, detect_edges_better

-Cameron Legree, 101153496 - green_channel, sepia, flip_horizontal, arguments_user_interface, save, batch_test_input



License: 
________

https://choosealicense.com/licenses/mit/
MIT License

Copyright (c) 2020 Akshay Vashisht, Mark Zachkewich, Jose Urieta, Cameron Legree

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
