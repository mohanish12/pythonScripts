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

##ParsingDictionaries.py
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
