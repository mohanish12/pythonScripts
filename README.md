

# pythonScripts
this repository contains python scripts written by me for various use cases

## findMedian.py
<p align="justify">
This script contains a function called findMedian which takes an input parameter of file which contains a set of numbers in each line. The function reads the file, generates 
a list of numbers from the files, sorts the list in ascending order and then return the median from the list. Here I have used statiscs module of python library to determine the 
median of the list
</p>

## next_fib.py
<p align="justify">
This scrit contains a function next_fib which takes two parameters as input- list of numbers, and the count of numbers to append to this list. It appends the count number of fibonacci integer in the sequence to the list and returns the new list
</p>

## AbstractNames.py
<p align="justify">
This script  has a function abstract_names which takes input parameter as a list of lists. Each list is a list of names each with a first name and a last name. The function returns a dictionary. The keys to the dictionary are the first names and the values are the list of the associated last names. The last names are sorted alphabetically.
</p>

## PingPong.py
<p align="justify">
The script has a function check_pingpong_winner which takes input parameter as a tuple of 2 integers. The first integer is Player 1 score and second integer is player 2 score. The function returns a string as per below:-

 - If Player 1 has won, return "Player 1 wins!"
 - If Player 2 has won, return "Player 2 wins!"
 - If neither player has won, return "Keep playing!"\
 </p>
 
## PositiveEvens.py
<p align="justify">
The script has a function count_positive_evens which takes input as a list of integers and returns output as a single integer. The number the function return is the count of numbers from the list that were both positive and even
</p>

## UpperCopy.py
<p align="justify">
the script has a function to_upper_copy which accepts two arguments 1. the input filename who content needs to read and converted to capital 2. The output file name where the contents read form file 1 are written into caps. Function does not return anything
</p>

## ParsingDictionaries.py
<p align="justify">
The script has a function check_value which accepts two arguments a dictionary to parse and a string to find. check_value looks of the string in the dictionary and get its value. The current value will always be a string. However check_value tries to convert it to an integer and a float, then return a message indicating the success of those transactions based on the below logic:-
- If the key is not found in the dictionary, check_value
  should return the string: "Not found!"
- If the value corresponding to the key can be converted
  to an integer, check_value should return the string:
  "Integer!"
- Otherwise, if the value corresponding to the key can be
  converted to a float, check_value should return the
  string: "Float!"
- Otherwise, check_value should return the string:
  "String!"
</p>  
  
## FindRange.py
<p align="justify">
The script contains a function called find_range which expects an argumnent of file name containing one integer per line. The function parses through the file and returns a tuple containing the minimum and maximum of integers in the file.
</p>

## PivotLibrary.py
<p align="justify">
The script contains a function called pivot_library which accepts one argument which is a list of n tuples. Each tuple in return has three items - the first item is a book title (a string), the second item is the books author ( a string), the third item is the books ISBN number (a string). pivot_library returns a dictionary in which the keys are the ISBN numbers and the values are two item tuples in which the first item is the book title and the second item is the books author name.
</p>

## BookInfo.py
<p align="justify">
The script contains a function called write_book_info which accepts two arguments - a string which represents the filename to write, a list of tuples in which each tuple contains three strings - book title, book author, book ISBN. The function writes the list of books to the filename using the below format:-

ISBN: Title by Author
</p>

## Rainfall.py
<p align="justify">
The script contains a function average_rainfall which has one parameter a list of intergers. The list represents daily rainfall measurements for a certain area. If the list has  a -1 at some point the average should stop and not consider any further readings. The function returns an integer with average of the readings
</p>

## RectangularPrism.py
<p align="justify">
The contains a function volume_and_area which takes in a dictionary. This dictionary is guarenteed to have three keys "length", "width" and "height" whose values are integers representing three attributes of a rectangular prism. The function modifies this dictionary to add two keys: "volume" and "area". The values associated with these keys should be the volume and surface area of the box. 
</p>

## DigitCount.py
<p align="justify">
The script contains a function called digit_count which takes input as a number, which could be either a float or an integer. It should return a dictionary whose keys are digits, and whose values are the number of times that digit appears in the number. The dictionary should not contain any numerals that do not appear at all in the number and it should not contain the decimal point character if the number is a decimal.
For example:

 digit_count(11223) -> {1: 2, 2: 2, 3: 1}
 
 digit_count(3.14159) -> {3: 1, 1: 2, 4: 1, 5: 1, 9: 1}
</p>

## ClassInfo.py
<p align="justify">
The script contains a function called write_class_data which will take as input two parameters: a string and a list of tuples. The string will represent the filename to which to write. Each 3-tuple in the list will contain three values:

 - A string representing the major of a college class (e.g.  "CS", "CHEM", "ENGL")
 
 - An integer representing a course number (e.g. 1301, 2241, 4001)
 
 - A string representing the name of a course (e.g.  "Introduction to Computing", "Organic Chemistry", etc.)
 
write_class_data writes the list of classes to the file given by the filename using the following format:

[major][number]: [class name]

So, for this list:

[("CS", 1301, "Introduction to Computing"), ("CHEM", "1310", "General Chemistry")]

The file printed would look like this:

CS1301: Introduction to Computing
CHEM1310: General Chemistry
</p>

## FindFirstLast2.py
<p align="justify">
The script contains a function called first_to_last which takes as input a string representing a filename. Inside the file would be some text on each line, some lines would contain integers , while others will contain strings of other characters. first_to_last would return a tuple containing the first and last strings in the file aplphabetically. It should ignore any lines that contain integers.
</p>

## Profile.py
<p align="justify">
The script contains a function called complete_profile. complete_profile takes as input a dictionary. This dictionary will have four keys first, middle, last and title. The function would return a dictionary with those four keys, and three more name, full_name, short_name. The values for those
keys should be:

- name: the first and last name, separated by a space
- full_name: the title, first, middle, and last names, with a space between each pair of strings
- short_name: the first letter of the first name, a space, and their last name
</p>

## FancyNames.py 
<p align="justify">
The script contains a function called fancy_me which takes as input a list of strings each representing a full name in the format "First Middle Last". It returns a single string formatting that list of names in fancy style like this - F. M. Last. Each individual name is the first initial, then a period, then a space, then the second initial, then a  period, then a space, then the last name, then a comma. There is no comma after the last name in the list.
</p>

## RockPaperScissors.py
<p align="justify">
The script contains a function called find_winner which takes as input a list of 2-tuples each representing a round of Rock-Paper-Scissors. Each 2-tuple will contain two strings.Each string will be either "Rock", "Paper", or "Scissors". The first item in the 2-tuple will represent what Player 1 chooses in each round, and the second item in the 2-tuple will represent what Player 2 chooses in each round. find_winner whould return the string "Player 1 wins!" if Player 1 wins more games than Player 2. It would return the
string "Player 2 wins!" if Player 2 wins more games than Player 1. It would return the string "It's a tie!" if the two players win an equal number of times. 
In the game Rock-Paper-Scissors, two opponents simultaneously choose to throw either "Rock", "Paper", or "Scissors". Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. If both players throw the same object, the round is a tie.
</p>
