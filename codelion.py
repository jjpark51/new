total_list = []

while True:
    question = input("Enter a question: ")
    if(question == "q"):
        break
    else:
        total_list.append({"Question" : question, "Answer": ""})
        
for i in total_list:
    print(i["Question"])
    answer = input("Enter answer: ")
    i["Answer"] = answer
print("=============================================")
print(total_list)
