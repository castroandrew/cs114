import sys
import random


print('')
print('')
print('')
print("welcome to Space Dungeon")
print("Press Enter To Continue")
input()
print('')

choose_your_class= 1
while choose_your_class== 1:
    print("Choose your Class")
    print('')
    print(" Space Duck")
    print('')
    print(" That One Human")
    print('')
    print(" Sexy Alien")
    classes = str(input())
    if classes != 'Space Duck' or 'That One Human' or 'Sexy Alien':
        print('please enter the class exactly')
        print('')
    elif:
        print('')
        choose_your_class= 0

Delegate_Ponts=1
while Delegate_Ponts==1
    print("Delegate Points. You have 100 to spend. ")
    print('')
    print("How Many points to magic")
    print('')
    magic = input()
    print('')
    print("How many points to attack")
    print('')
    attack =input()
    if int(magic)+ int(attack) != 100
        print('I am sorry but that does not add to 100. lets try agian.)
    elif int(magic) + int(attack) == 100
        Delegate_Ponts=0
    print('')




print("What is your name")
print('')
name = input()
print('')
print("Welcome " +name+ ", You have "+magic+" magic points and "+attack+ " attack points")
print("and is a "+classes+" class.")
print('')
print('')
health=100
enemies_health=80

# while health== 0:
    # print('you are dead')
    # sys.exit(0)
# this is the health block


# while magic== 0:
    # print('')
    # print(' you ran out of mp and past out.')
    # print('now your life is up to faith.')
    # if health== 0:
    #     int(magic) +1
    # else:
    #     print('you wake up with scars all over and bleeding. You retreat to live another day')
    # sys.exit(0)
    # what happens when you run out of mp

move='false'

# while move=='stats':
    print('')
    print('you have '+health+' hp left')
    print('and '+magic+' mp left')
    move='false'
    input()
    fight='fight'
    print('')
# this is the stats block

run= 'stay'

# while run== 'run':
#     print('You ran away like a wuss.')
#     sys.exit(0)
# Run away block

fight='false'

# while fight=='fight':
#     if health==0:
#         print('')
#         print('Nooooooo')
#     elif magic==0:
#         print('')
#         print('You feel sleepy')
#     elif enemies_health==0:
#         print('')
#         print('you did it. Now what were you in here for.')
#         print('')
#         print('')
#         print('all well, it must have not been that important.')
#         print('You left the room as a victor')
#         sys.exit(0)
# Fight check



print('')
print('you have enter a dull gray room in your ship.')
print('')
if classes== "Space Duck":
    print('It was then your mortal enemies attack ')
    print('The Ships CAT')
elif classes== "That One Human":
    print('It was then your mortal enemies attack ')
    print('That Guy')
elif classes== "Sexy Alien":
    print('It was then your mortal enemies attack ')
    print('reality')
# veryed text story
print('the fight begins')

print('what are you going to do fight or run')
fight= input()

while run== 'run':
    print('You ran away like a wuss.')
    sys.exit(0)
# Run away block

Battle= 'start'

def fighting():
    while Battle=='start:':
        while fight=='fight':
        if health==0:
            print('')
            print('Nooooooo')
        elif magic==0:
            print('')
            print('You feel sleepy')
        elif enemies_health==0:
            print('')
            print('you did it. Now what were you in here for.')
            print('')
            print('')
            print('all well, it must have not been that important.')
            print('You left the room as a victor')
            sys.exit(0)
        # Fight check
    # Fight check
        while fight=='fight':
        print(' your move. attack, magic, stats')
        move= input()
        if move== 'attack':
            print('you have attacked')
            attack_random= random.randint(1,5) + int(attack)
            print('you did'+ str(attack_random) +' damege.')
            enemies_health= int(enemies_health) - int(attack_random)
            move= 'over'
        elif move== 'magic':
            print('you have used magic')
            magic_random= random.randint(1,5)+ 20
            print('you did '+ str(magic_random) +' damege.')
            enemies_health= int(enemies_health) - int(magic_random)
            move= 'over'
        elif move == 'stats':
            print('')
            fight='pause'
        if move== 'over':
            print('Now they attack')
            fight= 'thier turn'
    # player fight phases block

        while move=='stats':
        print('')
        print('you have '+health+' hp left')
        print('and '+magic+' mp left')
        move='false'
        input()
        fight='fight'
        print('')
    # this is the stats block

        while fight=='fight':
        if health==0:
            print('')
            print('Nooooooo')
        elif magic==0:
            print('')
            print('You feel sleepy')
        elif enemies_health==0:
            print('')
            print('you did it. Now what were you in here for.')
            print('')
            print('')
            print('all well, it must have not been that important.')
            print('You left the room as a victor')
            sys.exit(0)
    # Fight check

        while fight=='fight':
        print(' your move. attack, magic, stats')
        move= input()
        if move== 'attack':
            print('you have attacked')
            attack_random= random.randint(1,5) + int(attack)
            print('you did'+ str(attack_random) +' damege.')
            enemies_health= int(enemies_health) - int(attack_random)
            move= 'over'
        elif move== 'magic':
            print('you have used magic')
            magic_random= random.randint(1,5)+ 20
            print('you did '+ str(magic_random) +' damege.')
            enemies_health= int(enemies_health) - int(magic_random)
            move= 'over'
        elif move == 'stats':
            print('')
            fight='pause'
        if move== 'over':
            print('Now they attack')
            fight= 'thier turn'
    # player fight phases block

        while enemies_health== 0:
        print(' They are dead')
        Battle='over'
    # this is the enemies_health block

        while magic== 0:
        print('')
        print(' you ran out of mp and past out.')
        print('now your life is up to faith.')
        if health== 0:
            int(magic) +1
        else:
            print('you wake up with scars all over and bleeding. You retreat to live another day')
            print('Game Over')
            sys.exit(0)
    # what happens when you run out of mp

        while fight== 'thier turn':
        health_hit= int(health - random.randint(25,40))
        health= int(health - health_hit)
        print('you took '+ str(health_hit) +' damege')
        if health <= 0:
            health = 0
            fight= 'game over'
        elif health >=0:
            fight='fight'
    # enemies fight phases block

        while fight=='fight':
        if health==0:
            print('')
            print('Nooooooo')
        elif magic==0:
            print('')
            print('You feel sleepy')
        elif enemies_health==0:
            print('')
            print('you did it. Now what were you in here for.')
            print('')
            print('')
            print('all well, it must have not been that important.')
            print('You left the room as a victor')
            sys.exit(0)
    # Fight check

        while health== 0:
        print('you are dead')
        sys.exit(0)
    # this is the health block
    # This is the Block for a battle

fighting()

print('')
print('You did it')
