"""Component 3 of Chinese and Japanese quiz
setup score counter
Created by Zach Wain
3/09/2020
"""

import random

# Setup some responses we can randomly choose between
correct_responses = ["Correct!", "Very good!", "Good work.", "Nice."]
incorrect_responses = ["Incorrect!", "Wrong answer."]

score_counter = 0
point_value = 10

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

# Tests
print(score_question("4", ["shi", "four", 4]))
print(score_question("four", ["shi", "four", 4]))
print(score_question("97", ["shi", "four", 4]))
print("total score: {}".format(score_counter))


