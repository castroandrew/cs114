import random
print('enter a number to see what it trully is')
base_number= len(input())
random_number = random.randint(1,15)
new_number= random_number + int(base_number)
print(new_number)
