"""Component 4 of Chinese and Japanese quiz
present final score to user and allow replay
Created by Zach Wain
04/09/2020
"""

score_counter = 50
number_of_questions = 10
point_value = 10
keep_playing = True

while keep_playing:
    # do normal game actions here...
    print("*** In the full game, this is where questions would be asked... ***")

    # game finished
    print("Your total score was: {} out of {}".format(score_counter, number_of_questions * point_value))
    decision = input("Would you like to play again (Y/N)? ")
    if decision.lower().startswith("n"):
        keep_playing = False
        print("Goodbye - thanks for playing!")

#note: create version 2 for summary (are you sure prompt)
