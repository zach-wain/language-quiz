"""Full program version 1 of Chinese and Japanese quiz
Assemble all components together
Created by Zach Wain
3/09/2020
"""

import random

score_counter = 0
point_value = 10
keep_playing = True

# This function scores the answer and returns a suitable message to show the user
def score_question(answer, number):
    if answer == number[1] or answer == str(number[2]):
        global score_counter
        score_counter = score_counter + point_value
        return "Correct! + {} points\n".format(point_value)
    else:
        return "Wrong answer.\n Correct answer is: {}\n".format(number[1])

# numbers for the different languages
# note: first and second list both have 'san' as three
Chinese = [["yi", "one", 1], ["er", "two", 2], ["san", "three", 3], ["si", "four", 4], ["wu", "five", 5],
           ["liu", "six", 6], ["qi", "seven", 7], ["ba", "eight", 8], ["jiu", "nine", 9], ["shi", "ten", 10]]
Japanese = [["ichi", "one", 1], ["ni", "two", 2], ["san", "three", 3], ["shi", "four", 4], ["go", "five", 5],
           ["roku", "six", 6], ["shichi", "seven", 7], ["hachi", "eight", 8], ["ku", "nine", 9], ["juu", "ten", 10]]

# main loop
while keep_playing:
    # start main game
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
    number_of_questions = len(shuffled_numbers)

    #loop through all the avaliable numbers
    for number in shuffled_numbers:
        answer = input("What number does {} stand for in English? ".format(number[0]))
        print(score_question(answer, number))

    # game finished
    print("Your total score was: {} out of {}".format(score_counter, number_of_questions * point_value))
    decision = input("Would you like to play again (Y/N)? ")
    if decision.lower().startswith("n"):
        keep_playing = False
        print("Goodbye - thanks for playing!")


#bug: score doesnt reset when game is replayed. needs to be fixed in version 2
