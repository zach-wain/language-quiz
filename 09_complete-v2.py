"""Full program version 2 of Chinese and Japanese quiz
Assemble all components together
Created by Zach Wain
5/09/2020
"""

import random

# variables
score_counter = 0
point_value = 10
keep_playing = True

# numbers for the different languages
# note: first and second list both have 'san' as three
chinese = [["yi", "one", 1], ["er", "two", 2], ["san", "three", 3], ["si", "four", 4], ["wu", "five", 5],
           ["liu", "six", 6], ["qi", "seven", 7], ["ba", "eight", 8], ["jiu", "nine", 9], ["shi", "ten", 10]]
japanese = [["ichi", "one", 1], ["ni", "two", 2], ["san", "three", 3], ["shi", "four", 4], ["go", "five", 5],
           ["roku", "six", 6], ["shichi", "seven", 7], ["hachi", "eight", 8], ["ku", "nine", 9], ["juu", "ten", 10]]

# Setup some responses we can randomly choose between
correct_responses = ["Correct!", "Very good!", "Good work.", "Nice."]
incorrect_responses = ["Incorrect!", "Wrong answer."]

# This function chooses a random response from the list it is given
def get_random_response(responses):
    return responses[random.randint(0, len(responses)-1)]

# This function scores the answer and returns a suitable message to show the user
def score_question(answer, number):
    if answer == number[1] or answer == str(number[2]):
        global score_counter
        score_counter = score_counter + point_value
        return "{} + {} points\n".format(get_random_response(correct_responses), point_value)
    else:
        return "{}\n Correct answer is: {}\n".format(get_random_response(incorrect_responses), number[1])

# This function judges the score and gives the player feedback
def judge_score():
    if score_counter >= point_value * number_of_questions:
        return "Excellent, you know your stuff!"
    elif score_counter >=70:
        return "Nice work, you're getting there!"
    elif score_counter >=30:
        return "You need some more practice"
    else:
        return "Are you even trying?"

# This function asks player a yes/no question and returns true/false
def ask_for_decision(question, positive_answer):
    decision = input(question)
    return decision.lower().startswith(positive_answer)

# Main loop
while keep_playing:
    # start main game
    quiz_type = input("Would you like to play a Chinese quiz or a Japanese quiz? ")
    if quiz_type == "Chinese" or quiz_type == "chinese":
        quiz_numbers = chinese
    elif quiz_type == "Japanese" or quiz_type == "japanese":
        quiz_numbers = japanese
    else:
        print("Please select either Japanese or Chinese")

    # Make a shuffled copy of our master number list
    shuffled_numbers = quiz_numbers.copy()
    random.shuffle(shuffled_numbers)
    number_of_questions = len(shuffled_numbers)

    # Loop through all the avaliable numbers
    for number in shuffled_numbers:
        answer = input("What number does {} stand for in English? ".format(number[0]))
        print(score_question(answer, number))

    # Game finished
    print("Your total score was: {} out of {}".format(score_counter, number_of_questions * point_value))
    print(judge_score())
    if ask_for_decision("Would you like to play again (Y/N)? ", "n"):
        if ask_for_decision("Are you sure you want to quit (Y/N)?", "y"):
            keep_playing = False
            print("Goodbye - thanks for playing!")



# bug: score doesnt reset when game is replayed. needs to be fixed in version 3
