import random
difficulty = ['easy']
questions1 = ['q1','q2','q3']
answers1 = ['a1','a2','a3']
def qset1():
    for i in range(2,-1,-1):
        n=random.randint(0,i)
        ans = input(questions1[n])
        if ans == answers1[n]:
            print('correct')
            questions1.remove(questions1[n])
            answers1.remove(answers1[n])
        else:
            print('wrong')
            return i
        if i==0:
            print("You have completed this segment of questions!")
def quiz_main_frame():
    user_difficulty = (input("chose your difficulty:"))
    if user_difficulty.lower() == 'easy':
        if difficulty[0]=='easy':
            difficulty[0]='easy_done'
            print('Questions are coming your way...')
            qset1()
        else:
            print('You have already attempted this segment')
            quiz_main_frame()
quiz_main_frame()
