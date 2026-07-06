print("="*30)
print("The General Knowledge Quiz ")        
print("="*30)
score=0
quiz=[{"question":"Which country has won the most cricket world cups? ","answer":"australia"},{"question":"Which is the largest country by area? ",
       "answer":"russia"},{"question":"What is the most famous sport in the world? ","answer":"football"}]

for q in quiz:
    user_answer=input(q["question"]).strip().lower()                                                 #q means question
    if(user_answer==q["answer"]):
        print("Well done!!!")
        score+=1
    else:
        print("Better luck next time...")
print(f"\nYour total score is {score} out of {len(quiz)}")