print('&&& Madlibs &&&')
print('==================================')
print('There once was a _____ From _____. ')
print(' Who dreamed that it was ____ a _____.')
print('it woke with a ____ ,in the middle of the night,')
print(' to see that its dream had come true.')
print('===================================')
print('please give a noun for line one')
line_one= input()
print('Would you like to see so far?')
view=input()

while view== yes:
    print('==================================')
    print('There once was a '+ str(line_one)+'From _____. ')
    print(' Who dreamed that it was ____ a _____.')
    print('it woke with a ____ ,in the middle of the night,')
    print(' to see that its dream had come true.')
    print('===================================')
    print('would you like to change line one?')
    change_line_one=input()
    if change_line_one==yes:
        print('please give a noun for line one')
        line_one= input()
    else:
        view=no




print('please give a place for line two')
line_two= input()
print('Would you like to see so far?')
view=input()

while view== yes:
    print('==================================')
    print('There once was a '+ str(line_one)+'From ' +str(line_two))
    print(' Who dreamed that it was ____ a _____.')
    print('it woke with a ____ ,in the middle of the night,')
    print(' to see that its dream had come true.')
    print('===================================')
    print('would you like to change line two?')
    change_line_two=input()
    if change_line_one==yes:
        print('please give a noun for line two')
        line_two= input()
    else:
        view=no





print('please give a adjective for line three')
line_three= input()
print('Would you like to see so far?')
view=input()

while view== yes:
    print('==================================')
    print('There once was a '+ str(line_one)+'From ' +str(line_two))
    print(' Who dreamed that it was '+str(line_three)+ ' a _____.')
    print('it woke with a ____ ,in the middle of the night,')
    print(' to see that its dream had come true.')
    print('===================================')
    print('would you like to change line three?')
    change_line_three=input()
    if change_line_three==yes:
        print('please give a noun for line three')
        line_three= input()
    else:
        view=no

print('please give a noun for line four')
line_four= input()
print('Would you like to see so far?')
view=input()

while view== yes:
    print('==================================')
    print('There once was a '+ str(line_one)+'From ' +str(line_two))
    print(' Who dreamed that it was '+str(line_three)+ 'a '+str(line_four))
    print('it woke with a ____ ,in the middle of the night,')
    print(' to see that its dream had come true.')
    print('===================================')
    print('would you like to change line four?')
    change_line_four=input()
    if change_line_four==yes:
        print('please give a noun for line four')
        line_four= input()
    else:
        view=no

print('please give a adjective for line five')
line_five= input()
print('Would you like to see so far?')
view=input()

while view== yes:
    print('==================================')
    print('There once was a '+ str(line_one)+'From ' +str(line_two))
    print(' Who dreamed that it was '+str(line_three)+ 'a '+str(line_four))
    print('it woke with a'+str(line_five)+ ',in the middle of the night,')
    print(' to see that its dream had come true.')
    print('===================================')
    print('would you like to change line five?')
    change_line_five=input()
    if change_line_five==yes:
        print('please give a noun for line five')
        line_five= input()
    else:
        view=no

print('Here is your Madlibs')
print('==================================')
print('There once was a '+ str(line_one)+'From ' +str(line_two))
print(' Who dreamed that it was '+str(line_three)+ 'a '+str(line_four))
print('it woke with a'+str(line_five)+ ',in the middle of the night,')
print(' to see that its dream had come true.')
print('===================================')
