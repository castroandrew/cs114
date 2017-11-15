import sys
import random


print('')
print('')
print('')
print("welcome to Space Dungeon")
print("Press Enter To Continue")
input()
print('')
print("Choose your Class")
print('')
print(" Space Duck")
print('')
print(" That One Human")
print('')
print(" Sexy Alien")
classes = str(input())
print('')
print("Delegate Points. You have 100 to spend. ")
print('')
print("How Many points to magic")
print('')
magic = input()
print('')
print("How many points to attack")
print('')
attack =input()
print('')
print("What is your name")
print('')
name = input()
print('')
print("welcome " +name+ "You have "+magic+" magic points and "+attack+ " attack points")
print("and is a "+classes+" class.")
print('')
print('')
health=100
enemies_health=80
while health== 0:
    print('you are dead')
    # this is the health block
    sys.exit(0)

while magic== 0:
    print('')
    print(' you ran out of mp and past out.')
    print('now your life is up to faith.')
    if health== 0:
        int(magic) +1
    else:
        print('you wake up with scars all over and bleeding. You retreat to live another day')
    sys.exit(0)
    # what happens when you run out of mp
move=false

while move==stats:
    print('')
    print('you have '+health+' hp left')
    print('and '+magic+' mp left')
    move=false
    input()
    fight=fight
    print('')
    # this is the stats block
run= stay
while run== run:
    print('You ran away like a wuss.')
    sys.exit(0)
    # Run away block

fight= false

while fight==fight:
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




print('')
print('you have enter a dull gray room in your ship.')

if classes==str(Space Duck):
    print('It was then your mortal enemies attack ')
    print('The Ships CAT')
elif classes== That One Human:
    print('It was then your mortal enemies attack ')
    print('That Guy')
elif classes== Sexy Alien:
    print('It was then your mortal enemies attack ')
    print('reality')

print('the fight begins')

print('what are you going to do fight or run')
fight= input()

while fight==fight:
    print(' your move. attack, magic, stats')
    move= input()
    if move== attack:
        print('you have attacked')
        attack_random= int(random.randint(1,5) + attack)
        print('you did'+attack_random+' damege.')
        enemies_health= int(enemies_health - attack_random + attack)
        move= over
    elif move== magic
        print('you have used magic')
        magic_random= int(random.randint(1,5)+ 20)
        print('you did'+magic_random+' damege.')
        enemies_health= int(enemies_health - magic_random)
        move= over
    elif move = stats
        print('')
        fight=pause
    if move== over:
        print('Now they attack')
        fight= thier turn
# player fight phases block

while fight== thier turn:
    health_hit= int(health - random.randint(25,40))
    health= int(health - health_hit)
    print('you took'+health_hit+' damege')
    if health <= 0
        health = 0
        fight= game over
    else
        fight=fight
# enemies fight phases block
