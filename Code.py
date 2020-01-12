
import random
import time
def montyhall():
    switch=True
    correct=0
    number_range=0
    timesrun=0
    switch_yes_or_no = input('Do you want to switch? Enter "y" or "n": ')
    if switch_yes_or_no == 'y':
        exit
    elif switch_yes_or_no == 'n':
        switch=False
    else:
        print('Must be y/n')
        switch_yes_or_no = input('Do you want to always say "no" when switching? y/n? ')
    number_range=int(input('What do you want the upper choice bound to be? '))
    while number_range<3:
        print('Must be 3+.\n')
        number_range=int(input('What do you want the upper choice bound to be? '))
    runamount=input('How many times should it be run? Press "x" for 1000. ')
    if runamount=='x':
        runamount=1000
    while timesrun<runamount:
        car = random.randint(1,number_range)
        player=random.randint(1,number_range)
        if player==car:
            if switch == True:
                timesrun+=1
            else:
                correct+=1
                timesrun+=1
        else:
            if switch== True:
                correct+=1
                timesrun+=1
            else:
                timesrun +=1
    percentage=correct/timesrun*100
    round(percentage,2)
    percentage = str(percentage)+'%'
    if switch == True:
        did_switch = '\n\tYou switched each time.'
    else:
        did_switch = '''\n\tYou didn't switch.'''
    print('||------------------------------------||',did_switch,'\n\tTimes run:',timesrun,'\n\tTimes player got car:',correct,'\n\tPercentage:',percentage,'\n||------------------------------------||\n')
    time.sleep(1)
    montyhall()
montyhall()

