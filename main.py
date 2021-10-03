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
        "answer" : ["The last prayer said on Yom Kippur, and it closes this day.", "A prayer that opens the new year and locks the previous one.", "The last prayer said on Yom Kippur, and it closes this day.", "A prayer that closes the last of the Tishrei holidays - Shemini Atzeret."],
        "answer_random" : ["A prayer recited on Simchat Torah when the Torah scrolls are locked in the Ark.", "A prayer that opens the new year and locks the previous one.", "The last prayer said on Yom Kippur, and it closes this day.", "A prayer that closes the last of the Tishrei holidays - Shemini Atzeret."]
    },
    6 : {
        "question" : "The 'worst days' is a nickname for: ",
        "answer" : ["The days from Rrosh hashanah to Yom Kipur which according to the bible is the days of law and sentence.", "all of the days in Teshrai that they are the law and sentence days.", "The Yom Kipurim war in 1973.", "The days in Elul when the slichot are said."],
        "answer_random" : ["The days from Rrosh hashanah to Yom Kipur which according to the bible is the days of law and sentence.", "all of the days in Teshrai that they are the law and sentence days.", "The Yom Kipurim war in 1973.", "The days in Elul when the slichot are said."],
    },
    7 : {
        "question" : "What is penance?",
        "answer" : ["A custom made by jewish before Yom kippur.", "A prayer that is said in Yom Kippur which the Jewish people request atonement for their wrongs.", "A phrase that is between a mother and her children.", "A collection of prayers and piyyutim to Yom Kippur."],
        "answer_random" : ["A custom made by jewish before Yom kippur.", "A prayer that is said in Yom Kippur which the Jewish people request atonement for their wrongs.", "A phrase that is between a mother and her children.", "A collection of prayers and piyyutim to Yom Kippur."],
    },
    8 : {
        "question" : "The Kol Nidrei prayer is: ",
        "answer" : ["A preayer that opens Yom kipur that is said before the sunsets.", "A prayer said if a jewish wants to Landor vows.", "A prayer said by a jewish when the tashlih ceramony occurs.", "A prayer that is being said in the forgivness days before Rosh hashanah"],
        "answer_random" : ["A preayer that opens Yom kipur that is said before the sunsets.", "A prayer said if a jewish wants to Landor vows.", "A prayer said by a jewish when the tashlih ceramony occurs.", "A prayer that is being said in the forgivness days before Rosh hashanah"]
    },
    9 : {
        "question" : "The jewish people celebrate Sukkot as a reminder for: ",
        "answer" : ["The meeting of the children of Israel in a Sukka after their departure from Egypt.", "The sukka that the children of Israel built in the asif season.", "The sukkot that were astablished by shephers in israel.", "The sukkot that were astablished by the pilgrims in jerusalem."],
        "answer_random" : ["The meeting of the children of Israel in a Sukka after their departure from Egypt.", "The sukka that the children of Israel built in the asif season.", "The sukkot that were astablished by shephers in israel.", "The sukkot that were astablished by the pilgrims in jerusalem."]
    },
    10 : {
        "question" : "The ushpizin is a nickname for: ",
        "answer" : ["The fathers of the nation according to tradition stay in the sukka.", "The four genders.", "Cooked vegetables that jewish people eat in Rosh hashanah eve.", "A tradition to make a festive holiday meal."],
        "answer_random" : ["The fathers of the nation according to tradition stay in the sukka.", "The four genders.", "Cooked vegetables that jewish people eat in Rosh hashanah eve.", "A tradition to make a festive holiday meal."]
    },
}


print("Hello and welcome to the rosh hashanah quiz!")
time.sleep(2)

points = 0


for quest in quiz:
    print(quiz[quest]['question'] + "\n")
    for ans in quiz[quest]['answer_random'] and range(4):
        The_chosen_one = random.choice(quiz[quest]['answer_random'])
        print(The_chosen_one + "\n")
        quiz[quest]['answer_random'].remove(The_chosen_one)
    user_res = input("Enter your answer: ")
    if user_res == quiz[quest]['answer'][0]:
        print(user_res)
        print("Correct! Good job! :)\n\n")
        points += 1
    else:
        print("Incorrect answer\n")
        print(f"The correct answer is: {quiz[quest]['answer'][0]}\n")

print(f"You got {points} questions right")
