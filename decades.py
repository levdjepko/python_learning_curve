# find out how many decades old is the person
age = int(input('How old are you?\n'))
decades = age // 10
remainder = age % 10
print ('You are ' + str(decades) + ' decades old, and ' + str(remainder) + ' years old')
