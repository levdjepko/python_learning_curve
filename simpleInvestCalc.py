# get user inputs
initialAmount = input ('Enter the initial investement amount\n')
time = input ('Enter the time in month for this investement\n')
additionalMonthly = input ('Enter the amount of monthly investment\n')
totalAmount = int (initialAmount)

# calculate the investment over time
for i in range(int(time)):
    totalAmount += totalAmount * 0.07 / 12 + float(additionalMonthly)

# show the result    
print (totalAmount)   
monthlyAmount = totalAmount*0.04/12
print ('Monthly is ' + '{0:.2f}'.format(monthlyAmount))
print (int(30 * 8000 * 0.01))
