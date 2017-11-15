import random 
def start():
    print('Ask me about your future')
    input()
    import random
    print("I will Now look into your FUTURE!!!")

# print(random.randint(1,15))
def eight_ball():
    Otext= "O" * random.randint(2,10)
    Mtext= "M" * random.randint(2,10)
    msg= Otext + Mtext
    return msg


def seeing():
    saw= eight_ball()
    print(saw)


"""
This work like a prayer.
"""





def The_Answer():
    fortune=random.randint(1,15)
    if fortune==1:
        fortune='It is certain'
    elif fortune==2:
        fortune='it is decidedly so'
    elif fortune==3:
        fortune='without a doubt'
    elif fortune==4:
        fortune='yes definitely'
    elif fortune== 5:
        fortune='You may rely on it'
    elif fortune==6:
        fortune=' Do not count on it'
    elif fortune==7:
        fortune=' My reply is no'
    elif fortune== 8:
        fortune='My sources say no'
    elif fortune==9:
        fortune=' Outlook not so good'
    elif fortune== 10:
        fortune='Very doubtful'
    elif fortune== 11:
        fortune='Reply hazy try again'
    elif fortune==  12:
        fortune='Ask again later'
    elif fortune==13:
        fortune='Better not tell you now'
    elif fortune== 14:
        fortune='Cannot predict now'
    elif fortune== 15:
        fortune='Concentrate and ask again'
    print(fortune)


def main():
    Starting= start()
    eight_ball_text= eight_ball()
    saw= seeing()
    output = The_Answer()


main()
