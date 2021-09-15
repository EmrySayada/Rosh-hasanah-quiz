import time
import random

quiz = {
    1 : {
        "question" : "The month of Teshrai according to the Bible is: ",
        "answer" : ["The 7 month of the year", "The 1 month of the year", "The 2 month of the year", "The 12 month of the year"],
        "answer_random" : ["The 7 month of the year", "The 1 month of the year", "The 2 month of the year", "The 12 month of the year"],
    },
    2 : {
        "question" : "The meaning of the term forgiveness: ",
        "answer" : ["Chapters of prayers and piyyutim that contain a request for forgiveness, recited in the month of Elul.", "A song that participated in the Hebrew Song Festival in 1977 and was sung by singer Yehudit Ravitz.", "Apology from a friend.", "A love song written by the poet Leah Goldberg in 1938"],
        "answer_random" : ["Chapters of prayers and piyyutim that contain a request for forgiveness, recited in the month of Elul.", "A song that participated in the Hebrew Song Festival in 1977 and was sung by singer Yehudit Ravitz.", "Apology from a friend.", "A love song written by the poet Leah Goldberg in 1938"]
    },
    3 : {
        "question" : "The symbols of Rosh Hashana are: ",
        "answer" : ["Apple in honey, pomegranate, vegetables like beets and leeks, fish head or lamb head.", "The seven species: wheat, barley, vine, fig, olive, pomegranate and honey.", "Dates, almonds, and all kinds of sweets.", "The four species: etrog, lulav, myrtle, willow."],
        "answer_random" : ["Apple in honey, pomegranate, vegetables like beets and leeks, fish head or lamb head.", "The seven species: wheat, barley, vine, fig, olive, pomegranate and honey.", "Dates, almonds, and all kinds of sweets.", "The four species: etrog, lulav, myrtle, willow."]
    },
    4 : {
        "question" : "Tashlih is: ",
        "answer" : ["A prayer said on Rosh Hashanah near a water mikveh, with a request to throw the iniquities into the water.", "The halachah of sages to bathe in the river on the eve of Rosh Hashanah.", "A prayer said on the evening of Yom Kippur", "Halacha of immersion in the mikveh for purification before Yom Kippur."],
        "answer_random" : ["A prayer said on Rosh Hashanah near a water mikveh, with a request to throw the iniquities into the water.", "The halachah of sages to bathe in the river on the eve of Rosh Hashanah.", "A prayer said on the evening of Yom Kippur", "Halacha of immersion in the mikveh for purification before Yom Kippur."]
    },
    5 : {
        "question" : "The lock pray is: ",
        "answer" : ["A prayer recited on Simchat Torah when the Torah scrolls are locked in the Ark.", "A prayer that opens the new year and locks the previous one.", "The last prayer said on Yom Kippur, and it closes this day.", "A prayer that closes the last of the Tishrei holidays - Shemini Atzeret."],
        "answer_random" : ["A prayer recited on Simchat Torah when the Torah scrolls are locked in the Ark.", "A prayer that opens the new year and locks the previous one.", "The last prayer said on Yom Kippur, and it closes this day.", "A prayer that closes the last of the Tishrei holidays - Shemini Atzeret."]
    },
}


print("Hello and welcome to the rosh hashanah quiz!")
time.sleep(2)

points = 0


for quest in quiz:
    print(quiz[quest]['question'] + "\n")
    for ans in quiz[quest]['answer_random'] and range(4):
        The_chosen_one = random.choice(quiz[quest]['answer_random'])
        print(The_chosen_one)
        quiz[quest]['answer_random'].remove(The_chosen_one)
    user_res = input("Enter your answer: ")
    if user_res == quiz[quest]['answer'][0]:
        print("Correct! Good job! :)\n\n")
        points += 1
    else:
        print("Incorrect answer\n\n")

print(f"You got {points} questions right")
