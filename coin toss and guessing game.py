import random
a=input('what game do you want to play, coin toss or guessing game.')
if a=='coin toss':
    e=0
    b=0
    l2=[]
    l3=[]
    while b!=10:
        b+=1
        l=['heads','tails']
        d=random.choice(l)
        l2.append(d)
        c=input('enter a guess heads or tails.')
        l3.append(c)
        if d==c:
            e+=1
            print('you guessed right')
        if b==10:
                print('you got',e,'guesses right.')
                print('computers guess',l2)
                print('what you said',l3)
f=0
if a=='guessing game':
    b=random.randint(0,30)
    
    while True:
        f+=1
        c=int(input('enter a number through 0 and 30'))
        if c==b:
            print('it took you',f,' attempts.')
            break
