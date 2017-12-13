import sys
import random

intro_list=['Welcome To Space Dungeon ','Press Enter To Continue ','Choose your Class Number '
,'1 Space Duck ','2 That One Human ','3 Sexy Alien ',' ','please type the number ',
'Delegate Points. You have 100 to spend. ','How Many points to magic ',
'How many points to attack ','I am sorry but that does not add to 100. lets try agian. ',
'What is your name? ']

fight_list=['you have enter a dull gray room in your ship ','Then you were attacked ',
'the fight begins','what are you going to do fight or run. ',
'your move. attack, magic, stats ','you have attacked ','you have used magic ',
'Now they attack ','you have ','hp left ','mp left ','you did ','you took ', 'damege. ']

end_list=['Nooooooo','You feel sleepy ','You ran away like a wuss. ','you did it. Now what were you in here for.',
'all well, it must have not been that important. ','You left the room as a victor ',
'They are dead','you ran out of mp and past out.','now your life is up to faith. ',
'you wake up with scars all over and bleeding. You retreat to live another day ',
'Game Over ','you are dead ']

player={
'hp': 100,
'attack': 0,
'magic': 0,
'name':'a'
'What_are_you':'a'
}

enemy1={
'hp':100,
'attack':50,
'name':'Grifgut'
}
def intro():
    print(intro_list[0])
    print(inro_list[1])
    input()
    print(intro_list[13])
    player{'name'}=input()

def what_are_you():
    print(intro_list[2])
    print(intro_list[3])
    print(intro_list[4])
    print(intro_list[5])
    print(intro_list[6])
    What_are_you=input()
    while What_are_you!=1 or 2 or 3
        print(intro_list[8])
        What_are_you=input()
    if What_are_you=1:
        player{'What_are_you'}=intro_list[4]
    if What_are_you=2:
        player{'What_are_you'}=intro_list[5]
    if What_are_you=3:
        player{'What_are_you'}=intro_list[6]

def points_delagation():
    magic_points=0
    attack_points=0
    while magic_points + attack_points!=100:
        print(intro_list[9])
        print(intro_list[10])
        magic_points=input()
        print(intro_list[11])
        attack_points=input()
        if magic_points + attack_points!=100:
            print(intro_list[12])
            print(intro_list[7])


# these first three factors work on setting a persons states

def end_hp():
    if player{'hp'}>=0:
        print(end_list[0])
        print(end_list[11])
        print(end_list[10])
    return    sys.exit(0)
def end_magic():
    if player{'magic'}>=0:
        print(end_list[1])
        print(end_list[7])
        print(end_list[9])
        print(end_list[10])
        return sys.exit(0)

def end_enemy1():
    if enemy1{'hp'}>=0
        print(end_list[6])
        print(end_list[3])
        print(end_list[10])
        return    sys.exit(0)


def GAME_OVER():
    end_magic()
    end_hp()
    end_enemy1()
    return Fight_Check()
# These are the end game points
def fight_intro():
    print(fight_list[0])
    print(fight_list[3]+' by a '+enemy1{'name'})
    if input()=run
        print(end_list[2])
        sys.exit(0)
    else:
        print(fight_list[2])

# This is the fight intro

def Fight_Check():
    while fight=='fight':
        print('--------------------------')
        print(fight_list[4])
        move= input()
        if move== 'attack':
            print(fight_list[5])
            attack_random= random.randint(1,5) + player{'attack'}
            print(fight_list[12]+ str(attack_random) +fight_list[14])
            enemy1{'hp'}= int(enemy1{'hp'}) - int(attack_random)
            move= 'over'
        elif move== 'magic':
            print(fight_list[6])
            magic_random= random.randint(1,5)+ 20
            player{'magic'}-5
            print(fight_list[12] + str(magic_random) +fight_list[14])
            enemy1{'hp'}= int(enemy1{'hp'}) - int(magic_random)
            move= 'over'
        elif move == 'stats':
            print('-----------------------')
            return stats()
        if move== 'over':
            print(fight_list[7])
            fight= 'thier turn'
            return enemy1_attack()
# Fight check


def stats():
    while move=='stats':
        print('')
        print(fight_list[9]+player{'hp'}+fight_list[10])
        print('and '+player{'magic'}+fight_list[11])
        move='false'
        input()
        fight='fight'
        print('')
        return Fight_Check()
# Stats block
def enemy1_attack():
    while fight== 'thier turn':
        health_hit= int(health - random.randint(25,40))
        player{'hp'}= int(health - health_hit)
        print(fight_list[13]+ str(health_hit) +fight_list[14])
        return GAME_OVER()
def Start_Game():
    intro()
    what_are_you()
    points_delagation()
    fight_intro()
    Fight_Check()

Start_Game()
