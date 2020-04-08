#hotel has 5 rooms
#room numbers - 101, 102, 103, 104, 105
#store the occupant_name for each room

#make sure you can do the following
#put someone in an unocupied room
#make a room available by setting occupant name to ''
#check if a room is occupied or not

#REFACTOR
#for any one room you should store the following
#occupant name
#phone number
#has prepaid - True False
#print room listings occupied or vacant

#allows for pprint.pprint(dict_name) which displays beautifully
import pprint

great_northwestern = {
    '101' : '',
    '102' : '',
    '103' : '',
    '104' : '',
    '105' : '',
}



bob = {
    'occupant_name': 'Bob',
    'phone_number': '4084132525',
    'has_prepaid': 'False',
}

great_northwestern['105'] = bob

#loop through rooms to display if they are occupied or vacant
for room_number in great_northwestern.keys():
    if great_northwestern[room_number] == '':
        print(f'{room_number} is vacant')
    else:
        print(f'{room_number} is occupied by {great_northwestern[room_number]["occupant_name"]}')



#function to create dictionary to be added to hotel dictionary
def create_occupant(room_number):
    if room_number == '':
        y_or_n = input(f'{room_number} is vacant, would you like to add an occupant? y/n')
        if y_or_n == 'y':
            great_northwestern[room_number]['occupant_name'] = input('What is the customers name? ')
            great_northwestern[room_number]['phone_number'] = input('What is the customers phone number? ')
            great_northwestern[room_number]['has_prepaid'] = input('Has the customer prepaid? y/n ')
                if y_or_n == 'y':
                    great_northwestern[room_number]['has_prepaid'] = True
                else:
                    great_northwestern[room_number]['has_prepaid'] = False
            

#prompt user if they would like to add a new customer
y_or_n = input('Would you like to add a new customer? y/n ')
if y_or_n == 'y':
    pass
else:
    pass


#loop through rooms to display if they are occupied or vacant
for room_number in great_northwestern.keys():
    if great_northwestern[room_number] == '':
        print(f'{room_number} is vacant')
    else:
        print(f'{room_number} is occupied by {great_northwestern[room_number]["occupant_name"]}')



#function adds key:value pairs into the dictionary 105
#  def add_to_105(room_number, name=''):
#     if room_number == '105':
#         occupant_name = input('Who would you like to add? ')
#         great_northwestern['105']['name'] = occupant_name
#         occupant_phone = int(input('What is their phone number?'))
#         great_northwestern['105']['phone number'] = occupant_phone
#         has_prepaid = input('Have they prepaid? y/n ')
#         if has_prepaid == 'y':
#             great_northwestern['105']['has prepaid'] == True
#         else:
#             great_northwestern['105']['has prepaid'] == False



# great_northwestern['101'] = 'Dale Cooper'
# great_northwestern['102'] = 'Laura Palmer'

# occupants_to_add = ['Audrey Horn', 'Laura Palmer', 'Log Lady', 'Pete Martell']


#function looks up room number and asks if youd like to assing it to anyone
#if you want to assign someone it calls assign() function below
# def occupied_or_not(room_number):
    # if great_northwestern[room_number] == '':
    #     print('This room is empty')
    #     assign(room_number, name='')
    # else:
    #     print(f'This room is occupied by {great_northwestern[room_number]}')
    #     to_assign = input(f'Who would you like to assign {room_number} to someone else? ')
    #     if to_assign != '':
    #         assign(room_number, name=to_assign)

#function looks up room number and asks who you would like to assign it to
# def assign(room_number, name=''):
    # if great_northwestern[room_number] == '':
    #     to_assign = input(f'Who would you like to assign {room_number} to? ')
    #     great_northwestern[room_number] = to_assign
        
    # else:
    #     great_northwestern[room_number] = name
    #     print(f'You\'ve assigned {room_number} to {name}')


#ask user which room they would like to look up
#then call the function occupied_or_not with the argument temp
# temp = input('Which room number would you like to look up? ')
# add_to_105(temp)
# print('The Great Northwestern')
# print('Current Occupants: ')
# for key in great_northwestern.keys():
#     print(f'Room # {key}: Occupant: {great_northwestern[key]}')