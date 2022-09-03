quiz={
    "question1":{
        "question":"What is capital of Turkey?",
        "answer":"Ankara"
    },
    "question2":{
        "question":"What is 2+2?",
        "answer":"4"

    },
    "question3":{
        "question":"What is capital of Germany?",
        "answer":"Berlin"

    },
    "question4":{
        "question":"What is capital of France?",
        "answer":"Paris"
    }


}
score=0
for key,value in quiz.items():
    print(value['question'])
    answer=input("Answer:")

    if value['answer'].lower()==answer.lower():
        print("correct!")
        score+=10
    else:
        print("false :( ")

print("TOTAL SCORE:{}".format(score))