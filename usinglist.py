total_dictionary = {}

while True:
    question = input("Enter question: ")
    if(question == "q"):
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("Enter Answer: ")
    total_dictionary[i] = answer
print(total_dictionary)