"""Component 4 of Chinese and Japanese quiz
present final score to user and allow replay
Created by Zach Wain
04/09/2020
"""

score_counter = 50
number_of_questions = 10
point_value = 10
keep_playing = True

def judge_score():
    if score_counter >= point_value * number_of_questions:
        return "Excellent, you know your stuff!"
    elif score_counter >=70:
        return "Nice work, you're getting there!"
    elif score_counter >=30:
        return "You need some more practice"
    else:
        return "Are you even trying?"

def ask_for_decision(question, positive_answer):
    decision = input(question)
    return decision.lower().startswith(positive_answer)

while keep_playing:
    # do normal game actions here...
    print("*** In the full game, this is where questions would be asked... ***")

    # game finished
    print("Your total score was: {} out of {}".format(score_counter, number_of_questions * point_value))
    print(judge_score())
    if ask_for_decision("Would you like to play again (Y/N)? ", "n"):
        if ask_for_decision("Are you sure you want to quit (Y/N)?", "y"):
            keep_playing = False
            print("Goodbye - thanks for playing!")


