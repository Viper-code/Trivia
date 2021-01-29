import random
import time
score = 0
q1='What runs but is always staionary? '
q2='What is the most disliked video on youtube? '
q3='How many letters are there in the Alphabet? '
q4='What is the tallest mountain in the world? '
q5='What is the biggest building in the world? '
q6='Write "all the numbers" in backwords: '
q7='Whats 2+4-2+4-2*0+0+2+7-6.2+778*0+0*0*0*0+100-6+5-7*0? '
q8='You’re running a race and at the very end, you pass the person in 2nd place. What place did you finish the race in? '
q9='I have a tail and a head, but no body. What am I? '
q10='Which word becomes shorter when you add 2 letters to it? '
q11='Which has more landmass: Antarctica or Canada?'
#q12=
#q13=
#q14=
#q15=

q_a = {q1:('river', 'treadmill'), q2:('yt rewind', 'youtube rewind', 'rewind'), q3:('8', 'eight'), q4:('everest', 'mt.everest'), q5:'burj khalifa', q6:'srebmun eht lla', q7:'0', q8:('2nd', 'second place', '2', 'second'), q9:('penny', 'coin'), q10:'short', q11:'antarctica'}
hints = {q1:'This thing is used for canoeing or fishing in', q2:"It's what youtube posted", q3:'count the letters in word Alphabet!', q4:'e--rest', q5:'b-rj k-al-fa', q6:'just write it backwords', q7:'always 0', q8:'not higher then first and lower then third place', q9:'its used in vending machines', q10:'shorten the word "shorter" just remove er', q11:'a-t-rct-ca'}
print('''                               Hello and welcome to the Trivia Game!                             
     In this trivia game you can choose how many questions you want below this text.You will get
     one point if you get a question right and you wont get a point if you get it wrong, and btw you got 30 sec for each questions!GoodLuck''')
num_q = input('                   Please enter the amount of questions you want from 2-10: ')

for i in random.choices(list(q_a), k=int(num_q)):
    print()
    print(i)
    now = time.time()

#BLOCK OF HINTS/SKIP
    flag1 = input('Do you want to skip the question? (y/n): ')    #skipping a question
    if flag1=='y':                                                 #skipping a question
        continue
    flag2 = input('Do you want to get a hint but you will lose 1 point! (y/n): ') #hints
    if flag2=='y':
        score = score-1
        print(hints[i])

    
#BLOCK OF ANS/WRONG
    ans = input('please enter the answer for this question: ')
    if ans in q_a[i]:
        score = score +1
        print()
        print('correct!you got 1 point.you have',score,'points!')
    elif ans != q_a[i]:
        print()
        print('Ooops you got it wrong D: you got 0 points.your score so far is ',score,'!')

#quit the game?
    flag3 = input('Do you want to Quit the game? (y/n): ')
    if flag3=='y':
        break
print('Your final score is ',score,'/',num_q)
print(f'It took you {round(time.time()-now)} seconds to complete the quiz, which had',num_q,'question(s)!')
input('Please Enter To EXIT ')
