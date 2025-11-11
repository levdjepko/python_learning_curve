# dictionaries in Python
contacts = {
    'number':4,
    'students':
    [
        {'name':'Sarah Connor', 'email':'sarah@example.com'},
        {'name':'Harry Potter', 'email':'harryp@example.com'},
        {'name':'John Connor', 'email':'johny@example.com'},
        {'name':'Ronald McDonald', 'email':'McD@example.com'},
        {'name':'John Johns', 'email':'jj@johnys.com'}
    ]
}
print('Student emails:')
for student in contacts['students']:
    print (student['email'])
