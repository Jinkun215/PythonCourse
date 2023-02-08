import json

with open("files/questions.json", "r") as file:
    content = file.read()

#print(content)

data = json.loads(content)  #sort through the string, and identify the list/dict
print(type(content))  #prints string
print(type(data))     #prints list
score = 0

for question in data:
    print(question["question_Text"])
    for index, alternatives in enumerate(question["alternatives"]):
        print(index + 1, "-", alternatives)
    user_choice = int(input("Enter your answer: "))
    # if (user_choice  == question["correct_answer"]):
    #     print("Correct!")
    # else:
    #     print("Incorrect")
    question["user_input"] = user_choice    #this method stores the input
    if question["user_input"] == question["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect"
              "")


print("\n", score)