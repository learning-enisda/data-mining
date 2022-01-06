# Season Check 

mount = str(input('Enter the month name in lowercase : '))
if mount == 'september' or mount == 'oktober' or mount == 'november':
    print('Autumn')
elif mount == 'december' or mount == 'january' or mount == 'february':
    print('Winter')
elif mount == 'march' or mount == 'april' or mount == 'may':
    print('Spring')
elif mount == 'june' or mount == 'july' or mount == 'august':
    print('Summer')
else:
    print('Please recheck the name of the month you wrote down')