"""Component 2 of Chinese and Japanese quiz
randomly generate 10 questions
Created by Zach Wain
27/08/2020
"""

import random

# 1st list
Chinese = [["yi", "one", 1], ["er", "two", 2], ["san", "three", 3], ["si", "four", 4], ["wu", "five", 5],
           ["liu", "six", 6], ["qi", "seven", 7], ["ba", "eight", 8], ["jiu", "nine", 9], ["shi", "ten", 10]]

#2nd list
Japanese = [["ichi", "one", 1], ["ni", "two", 2], ["san", "three", 3], ["shi", "four", 4], ["go", "five", 5],
           ["roku", "six", 6], ["shichi", "seven", 7], ["hachi", "eight", 8], ["ku", "nine", 9], ["juu", "ten", 10]]

#note: first and second list both have 'san' as three#

quiz_type = input("Would you like to play a Chinese quiz or a Japanese quiz? ")
if quiz_type == "Chinese" or quiz_type == "chinese":
    quiz_numbers = Chinese
elif quiz_type == "Japanese" or quiz_type == "japanese":
    quiz_numbers = Japanese
else:
    print("Please select either Japanese or Chinese")

# make a shuffled copy of our master number list
shuffled_numbers = quiz_numbers.copy()
random.shuffle(shuffled_numbers)

score_counter = 0

for number in shuffled_numbers:
    answer = input("What number does {} stand for in English? ".format(number[0]))
    if answer == number[1] or answer == str(number[2]) :
        print("Correct answer!\n")
    else:
        print("incorrect\n correct answer is {}".format(number[1]))
