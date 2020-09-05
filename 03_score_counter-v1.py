"""Component 3 of Chinese and Japanese quiz
setup score counter
Created by Zach Wain
3/09/2020
"""

score_counter = 0
point_value = 10

# This function scores the answer and returns a suitable message to show the user
def score_question(answer, number):
    if answer == number[1] or answer == str(number[2]):
        global score_counter
        score_counter = score_counter + point_value
        return "Correct! + {} points\n".format(point_value)
    else:
        return "Wrong answer.\n Correct answer is: {}\n".format(number[1])

# Tests
print(score_question("4", ["shi", "four", 4]))
print(score_question("four", ["shi", "four", 4]))
print(score_question("97", ["shi", "four", 4]))
print("total score: {}".format(score_counter))


