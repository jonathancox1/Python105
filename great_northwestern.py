#hotel has 5 rooms
#room numbers - 101, 102, 103, 104, 105
#store the occupant_name for each room

#make sure you can do the following
#put someone in an unocupied room
#make a room available by setting occupant name to ''
#check if a room is occupied or not

great_northwestern = {
    '101' : '',
    '102' : '',
    '103' : '',
    '104' : '',
    '105' : '',
}

great_northwestern['101'] = 'Dale Cooper'
great_northwestern['102'] = 'Laura Palmer'

occupants_to_add = ['Audrey Horn', 'Laura Palmer', 'Log Lady', 'Pete Martell']

#function looks up room number and asks if youd like to assing it to anyone
#if you want to assign someone it calls assign() function below
def occupied_or_not(room_number):
    if great_northwestern[room_number] == '':
        print('This room is empty')
        assign(room_number, name='')
    else:
        print(f'This room is occupied by {great_northwestern[room_number]}')
        to_assign = input(f'Who would you like to assign {room_number} to someone else? ')
        if to_assign != '':
            assign(room_number, name=to_assign)

#function looks up room number and asks who you would like to assign it to
def assign(room_number, name=''):
    if great_northwestern[room_number] == '':
        to_assign = input(f'Who would you like to assign {room_number} to? ')
        great_northwestern[room_number] = to_assign
        
    else:
        great_northwestern[room_number] = name
        print(f'You\'ve assigned {room_number} to {name}')


#ask user which room they would like to look up
#then call the function occupied_or_not with the argument temp
temp = input('Which room number would you like to look up? ')
occupied_or_not(temp)
print('The Great Northwestern')
print('Current Occupants: ')
for key in great_northwestern.keys():
    print(f'Room # {key}: Occupant: {great_northwestern[key]}')