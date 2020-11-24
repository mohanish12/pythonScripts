# pythonScripts
this repository contains python scripts written by me for various use cases

## findMedian.py
This script contains a function called findMedian which takes an input parameter of file which contains a set of numbers in each line. The function reads the file, generates 
a list of numbers from the files, sorts the list in ascending order and then return the median from the list. Here I have used statiscs module of python library to determine the 
median of the list

## next_fib.py
This scrit contains a function next_fib which takes two parameters as input- list of numbers, and the count of numbers to append to this list. It appends the count number of fibonacci integer in the sequence to the list and returns the new list

## AbstractNames.py
This script  has a function abstract_names which takes input parameter as a list of lists. Each list is a list of names each with a first name and a last name. The function returns a dictionary. The keys to the dictionary are the first names and the values are the list of the associated last names. The last names are sorted alphabetically.

## PingPong.py
The script has a function check_pingpong_winner which takes input parameter as a tuple of 2 integers. The first integer is Player 1 score and second integer is player 2 score. The function returns a string as per below:-

 - If Player 1 has won, return "Player 1 wins!"
 - If Player 2 has won, return "Player 2 wins!"
 - If neither player has won, return "Keep playing!"\
 
## PositiveEvens.py
The script has a function count_positive_evens which takes input as a list of integers and returns output as a single integer. The number the function return is the count of numbers from the list that were both positive and even

## UpperCopy.py
the script has a function to_upper_copy which accepts two arguments 1. the input filename who content needs to read and converted to capital 2. The output file name where the contents read form file 1 are written into caps. Function does not return anything

## ParsingDictionaries.py
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
  
  
## FindRange.py
The script contains a function called find_range which expects an argumnent of file name containing one integer per line. The function parses through the file and returns a tuple containing the minimum and maximum of integers in the file.

## PivotLibrary.py
The script contains a function called pivot_library which accepts one argument which is a list of n tuples. Each tuple in return has three items - the first item is a book title (a string), the second item is the books author ( a string), the third item is the books ISBN number (a string). pivot_library returns a dictionary in which the keys are the ISBN numbers and the values are two item tuples in which the first item is the book title and the second item is the books author name.

## BookInfo.py
The script contains a function called write_book_info which accepts two arguments - a string which represents the filename to write, a list of tuples in which each tuple contains three strings - book title, book author, book ISBN. The function writes the list of books to the filename using the below format:-

ISBN: Title by Author

## Rainfall.py
The script contains a function average_rainfall which has one parameter a list of intergers. The list represents daily rainfall measurements for a certain area. If the list has  a -1 at some point the average should stop and not consider any further readings. The function returns an integer with average of the readings

## RectangularPrism.py
The contains a function volume_and_area which takes in a dictionary. This dictionary is guarenteed to have three keys "length", "width" and "height" whose values are integers representing three attributes of a rectangular prism. The function modifies this dictionary to add two keys: "volume" and "area". The values associated with these keys should be the volume and surface area of the box. 

## DigitCount.py
The script contains a function called digit_count which takes input as a number, which could be either a float or an integer. It should return a dictionary whose keys are digits, and whose values are the number of times that digit appears in the number. The dictionary should not contain any numerals that do not appear at all in the number and it should not contain the decimal point character if the number is a decimal.
For example:

 digit_count(11223) -> {1: 2, 2: 2, 3: 1}
 
 digit_count(3.14159) -> {3: 1, 1: 2, 4: 1, 5: 1, 9: 1}
