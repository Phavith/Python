#File name is Quiz_app.py

#get user response :: input function

total_point = 0
name = input("What is your name? ")
print("Hello", name)

#compare response and answer
question = input("2 + 2? ")

if question == "4":
    total_point = total_point + 1
    print('Correct. :D')
else:
    print("Incorrect. :(")


question = input("What is the capital of France? ")
if question.lower() == "paris":
    total_point = total_point + 1
    print('Correct. :D')
else:
    print("Incorrect. :(")


question = input("Where is Sydney located? ")
if question.lower() == "australia":
    total_point = total_point + 1
    print('Correct. :)')
else:
    print('Incorrect. :)')

question = input("Who was the person that invented the concept of gravity? ")
if question.lower() == "isaac newton":
    total_point = total_point + 1
    print('Correct. :D')
else:
    print("Incorrect. :(")


question = input("What continent is Cambodia located? ")
if question.lower() == "asia":
    total_point = total_point + 1
    print('Correct. :D')
else:
    print("Incorrect. :(")

print("RESULT: ")
print(f"your total point is: {int(total_point/5*100)}% Good job!")
