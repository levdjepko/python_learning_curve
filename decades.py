# find out how many decades old the person is
age = int(input('How old are you?\n'))
decades = age // 10   # integer division - Python3 version
remainder = age % 10
print ('You are ' + str(decades) + ' decades old, and ' + str(remainder) + ' years old')
