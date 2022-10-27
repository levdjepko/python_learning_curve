# get user inputs
initialAmount = input ('Enter the initial investement amount\n')
time = input ('Enter the time in month for this investement\n')
additionalMonthly = input ('Enter the amount of monthly investment')
totalAmount = int(initialAmount)

# calculate the investment over time
for i in range (int(time)):
    totalAmount += totalAmount * 0.07 / 12 + additionalMonthly

# show the result    
print (totalAmount)    
