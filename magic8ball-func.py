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
    fortune=random.randint(0,14)
    fortune_answers= ['It is certain','it is decidedly so','without a doubt',
    'yes definitely','You may rely on it',' Do not count on it',' My reply is no','My sources say no',
    ' Outlook not so good','Very doubtful','Reply hazy try again','Ask again later',
    'Better not tell you now','Cannot predict now','Concentrate and ask again']
    print(fortune_answers[fortune])



def main():
    Starting= start()
    eight_ball_text= eight_ball()
    saw= seeing()
    output = The_Answer()


main()
