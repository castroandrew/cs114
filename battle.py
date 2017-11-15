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
# This is the Block for a battle for space dungeon 
