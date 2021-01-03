

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

# Algorithmic Scripts

## PalindromeChecker.py
The script contains a function called is_palindrome. The function has one parameter a string. The function returns TRUE if string is palindrome, FALSE if not. Assume that the only characters in the string are letters, spaces, apostrophes, commas, periods and question marks

## NotList.py
The script contains a function called not_list which has two parameters- a list of booleans and a list of integers. The list of integers would represent the indices for the list of booleans. not_list would switch the values of all the booleans located at those indices. 
For example:
bool_list = [True, False, False]
index_list = [0, 2]
not_list(bool_list, index_list) -> [False, False, True]


## CountSqaures.py
The script contains a function called count_squares which takes as input a list of integers and returns as output a single integer. The number the function returns is the number of perfect squares it found in the list of integers. Check the algorithm used for this script [here](https://github.com/mohanish12/algorithms/blob/main/perfect_sqaure.md)

## PalindromeBuilder.py
The script contains a function called create_palindrome which has one parameter a string and returns one string as a palindrome. If the string was not already a palindrome, the function returns a new string made from the original string and the reverse of the original string.
Eg. reate_palindrome("abc") -> "abccba"
However if the string is already a palindrome the function just returns the original string by itself. In determining whether the string is a palindrome or not, the function ignores punctuation, capitalization, spaces, comma, aspostrophe and question marks


## NegateList.py
The script contains a function called negate_list which has two parameters - a list of floats and a list of integers. The list of integers represents indices for the list of floats. negate_list switches the sign of all the floats located at those indices

## PointlessCopy.py
The script contains a function called copy_pointless which takes two paramters both strings. The first string is the filename of the file to which to write and the second string is the filename of the file from which to read. copy_pointlessly copies the contents of input_file to output_file but makes the following changes:-
- Replace all instances of the letter A (either capital or
   lower case) with the at sign, @
 - Replace all instances of the letter M (either capital or
   lower case) with the character sequence |\/|
 - Replace all instances of the letter W with the character
   sequence \/\/
 - Replace all instances of the letter O (either capital
   or lower case) with the numeral 0
 - Alternate the case for every remaining letter in the
   string (hint: the_string.swapcase() returns the string
   with the case of all letters swapped)

## InventorySearch.py
The script contains a function called sufficient_inventory which takes three parameters- a list of instances of InventoryItem representing the current inventory, an item name (a string) and a desired quantity (an integer). The function returns true if the below two conditions are met:-
- There exists an instance of InventoryItem in the list whose name matches the the item name parameter.
- The quantity associated with that instance is larger than the desired quantity.

## Uno.py
The game Uno is a card game where each players goal is to get rid of all their cards. A round ends when the player has gotten rid of all their cards. They then receive a number of points based on the cards left on their opponents hands. The first player to reach 500 points across multiple rounds wins the game.
The script containes a function called check_uno_winner which takes one parameter- a tuple with at least two integers but up to 8. Each integer wil represent one player's score. If any player has more than 500 points , check_uno_winner returns the string "Player X wins!" where X is the position of the player in the list who has more than 500 points. If no player has more than 500 points check_uno_winner returns "keep playing!"

## findGCF.py
The script contains a function called find_gcf which has two parameters both intergers. The function returns the Greatest Common Factor (GCF) of those two numbers.

## PigLatin.py
PigLatin is a fictitious language. To translate a word into Pig Latin, you would take the consonants up until the first vowel, move them to the end, and add "ay" to the end. The script contains a function called to_pig_latin which takes as input a single word, and return the Pig Latin version of the word.


## DeleteList.py
The script contains a function delete_from_list which has two parameters - a list of string and a list of integers. The list of integers represent the indices of the items to delete from the list of strings. The function deletes the item from the list of strings and returns the resulting list

## ExpandingDictionaries.py
The script contains a function called add_to_dictionary which has three parameters- a dictionary, a potential new key, and a potential new value. The function adds the given key and value to the dictionary if the key is of a legal type to be used as a dictionary key and return the resultant dictionary. If the key is not a legal type to be used as a dictionary key return the string "Error!"

## Horse.py
The game HORSE is a popular basketball shooting game. It can be played with any number of players. One by one each player takes a shot from anywhere they want. If they make the shot, the next person must make a shot. If they do not, they receive a letter: H, then O, then R, then S, then E. Once a player receives all five letters, they are out of the game.  The game continues until all but one player has all five letters.
The script contains function check_horse_winner which takes as input a tuple of at least 2, but potentially more, strings. 
check_horse_winner returns the following:-
- If only one player is left with fewer than 5 letters,
  return "Player X wins!", where X is the index of the
  player in the list (which could be 0).
- If more than one player has fewer than 5 letters,
  return "Players X, Y: keep playing!", where X, Y, and
  potentially more numbers are the indices of all players
  who have not yet been eliminated.
- If no player has 5 letters, return "Everyone: keep
  playing!"
  
## CapitalConsonants.py
The script contains a function called count_capital_consonants which takes as input a string and returns as output a single integer. The number the function returns is the count of characters from the string that were capital consonants.

