# A program that asks one user a question and stores the responses
import json
# Part 1 Generate the questions you want to ask one user

# responses = {
# }
#
# responses["name"] = input("What's your name? ")
# responses["age"] = input("How old are you? ")
# responses["city"] = input("What city do you live in? ")
# responses["birthmonth"] = input("What is your birth month? ")
# responses["food"] = input("What's your favorite food? ")
# responses["color"] = input("What's your favorite color? ")
# print(responses)

# Part 1 Create something to store the responses (hint: not a list but something that has key-value pairs)


questions = [
"What's your name?",
"How old are you?",
"What city do you live in?",
"What is your birth month?",
"What is your favorite food?",
"What's your favorite color?",
"What's your password?",
"What's your favorite historical era?",
"Favorite meme?"
]

listOfAnswers=[]
finished = "no"
while finished == "no":

    answers = {}
    keys = ["name", "age", "city", "birthmonth", "food", "color", "pw", "era", "meme"]

    for q in range(len(questions)):
        response = input(questions[q]+" ")
        answers[keys[q]] = response

    listOfAnswers.append(answers)

    done = input("Would you like to take the survey again? ")
    if done == "yes" or done== "Yes" or done == "YES":
        finished = "no"
    else:
        finished = "yes"

# print(answers)
# Part 1 ask the questions and store thee responses

# Part 1 Display the responses to check if the program is working

file = open("completedresponses.json","r")
oldData = json.load(file)
listOfAnswers.extend(oldData)
file.close()


# Other things to think about: how might I catch invalid or blank responses?

file = open("completedresponses.json","w")
file.write("[\n")
index = 0
#goes through each of answers in list of answers. if not last, comma inserted; otherwise pagebreak
for answer in listOfAnswers:
    if index < (len(listOfAnswers)-1):
        json.dump(answer,file)
        file.write(",\n")
    else:
        json.dump(answer, file)
        file.write("\n")
    index += 1

file.write("\n]")
file.close()


# Part 2 change the above program to allow more than one response

# Part 3 open the json file and load all old data to the new dataset.
# Don't forget to close the file after you open!


# Part 3 reopen the file and write each set of responses in json format
# Think about what separates each set of responses. Is that included at the end of the last item?
