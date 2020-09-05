"""Component 1 of Chinese and Japanese quiz
Ask if user wants to do a Chinese or Japanese quiz
Created by Zach Wain
27/08/2020
"""


# 1st list
Chinese = [["yi", "one"], ["er", "two"], ["san", "three"], ["si", "four"], ["wu", "five"],
           ["liu", "six"], ["qi", "seven"], ["ba", "eight"], ["jiu", "nine"], ["shi", "ten"]]

#2nd list
Japanese = [["ichi", "one"], ["ni", "two"], ["san", "three"], ["shi", "four"], ["go", "five"],
           ["roku", "six"], ["shichi", "seven"], ["hachi", "eight"], ["ku", "nine"], ["juu", "ten"]]

#note: first and second list both have 'san' as three#

quiz_type = input("Would you like to play a Chinese quiz or a Japanese quiz? ")
if quiz_type == "Chinese" or quiz_type == "chinese":
    quiz_type = Chinese
elif quiz_type == "Japanese" or quiz_type == "japanese":
    quiz_type = Japanese
else:
    print("Please select either Japanese or Chinese")
