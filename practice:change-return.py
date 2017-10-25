quarters = 25
dimes = 10
nickels = 5
pennies = 1
print('input amount')
total= input()
total_quarters = int(total) // quarters
total_dimes= (int(total)- (total_quarters * 25)) // dimes
total_nickels= (int(total)- (total_quarters * 25)-(total_dimes * 10))// nickels
total_pennies= (int(total)- (total_quarters * 25)-(total_dimes * 10)-(total_nickels*5))// pennies
str(total_quarters)
str(total_dimes)
str(total_nickels)
str(total_pennies)
print('your change is '+str(total_quarters)+" quarters")
print(str(total_dimes)+" dimes")
print(str(total_nickels)+" nickels")
print(str(total_pennies)+" pennies")
print('now shut up and take my money! ')
