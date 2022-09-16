name = ''

while not name:
    print('Enter your name:')
    name = input()
print('how many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('be sure to have enough room for your guests!')
print('Done')