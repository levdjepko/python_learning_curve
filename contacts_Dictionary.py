contacts = {
    'number' :4,
    'students':
    [
        {'name':'Sarah Connor', 'email':'sarah@example.com'},
        {'name':'Harry Potter', 'email':'harryp@example.com'},
        {'name':'John Connor', 'email':'johny@example.com'},
        {'name':'Ronald McDonald', 'email':'MCD@example.com'}
    ]
}

print('Student email:')
for student in contacts['students']:
    print (student['email'])
