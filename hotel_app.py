import pprint
# Setup, create menues
main_menu = '''
Home Menu------
1. Print Room Status
2. Check-In a customer
3. Check-Out a customer
4. Admin Features
5. Exit

'''
check_in_menu = '''
Check In------
1. Print Room Status
2. Add Customer Info
3. Request Room Specifics
4. Exit

'''
check_out_menu = '''
Check Out------
1. Print Room Status
2. Check Out of Room#
3. Exit

'''
admin_menu = '''
Admin------
1. Print Guest List
2. Save Hotel Info
3. Load Hotel Info
4. Check if room vacant
5. Exit

'''
#Setup define functions
#checks to is if room is vacant
def is_vacant(location, room_number):
    if hotels[location][room_number] == '':
        print('This Room is vacant')
    else:
        print(f'{room_number} is occupied by {hotels[location][room_number]}')
#function that checks in guest, assigning them to room number        
def check_in(number, guest, which_location):
    hotels[which_location][number] = guest
#function that checks out guest, removes them from the corresponding key room number
#include the print() in the function or else there will be nothing to bring after function runs!
def check_out(number,):
    print(f'{hotels[0][number]} has been checked out of room {number}')
    hotels[0][number] = ''

#Setup create hotel location dictionaries
hotel_atlanta = {
        'name' : 'atlanta',
        '101' : '',
        '102' : '',
        '103' : '',
        '104' : '',
        '105' : '',
}
hotel_boston = {
        'name' : 'boston',
        '101' : '',
        '102' : '',
        '103' : 'test',
        '104' : '',
        '105' : '',
}
hotel_barcelona = {
        'name' : 'barcelona',
        '101' : 'test',
        '102' : '',
        '103' : '',
        '104' : '',
        '105' : '',
}
hotels = [hotel_atlanta, hotel_boston, hotel_barcelona]
guests = []


#Begin
while True:
    menu_choice = int(input(main_menu))
    # 1. Room Status
    if menu_choice == 1:
        count = 0
        for location in hotels:
            for room_number in hotels[0].keys():
                if hotels[count][room_number] == '':
                    print(f'{room_number} is vacant')
                else:
                    print(f'{room_number} is occupied by {hotels[count][room_number]}')
            count += 1


    # Check In Menu
    elif menu_choice == 2:
        while True:
            menu_choice = int(input(check_in_menu))
        
            # Print Room Status
            if menu_choice == 1:
                count = 0
                for location in hotels:
                    for room_number in hotels[0].keys():
                        if hotels[count][room_number] == '':
                            print(f'{room_number} is vacant')
                        else:
                            print(f'{room_number} is occupied by {hotels[count][room_number]}')
                    count += 1
            
            # Add Customer Info
            elif menu_choice == 2:
                #create a dictionary with the guests last name
                #formatted like this
                # guests_last_name = {
                #   'name' : 'firstname lastname',
                #   'phone_number' : '109520358',
                #   'has_prepaid' : 'yes',
                # }
                guest_last_name = input('What is the guests last name? ')
                guests_first_name = input('What is the guets first name? ')
                guest_name = f'{guests_first_name} {guest_last_name}'
                #creates dictionary
                which_location = int(input('Which location are they checking into? '))
                guest_last_name = {}
                guest_last_name['name'] = f'{guest_name}'
                guest_phone = input('What is the guests phone number? ')
                guest_last_name['phone_number'] = guest_phone
                has_prepaid = input('Has the guest prepaid? ')
                guest_last_name['has_prepaid'] = has_prepaid
                #what room number to assing this dictionary to?
                room_num = input(f'What room shall we assign {guest_last_name["name"]} to? ')
                #call the function check_in
                check_in(room_num, guest_name, which_location)
                #append the guests list with the dictionary for future reference
                guests.append(guest_last_name)
                # print(hotels[0][room_num][name])

            
                # room_number = input('Which Room Number? ')
                # guest_name = input('Guests Name? ')
                # check_in(room_number, guest_name)
                # print(f'{hotels[0][room_number]} has been checked in to room {room_number}')
                
            # Request Room Specifics
            elif menu_choice == 3:
                pass
            
            #Exit
            elif menu_choice == 4:
                break

        
    # 3. Check Out Menu
    elif menu_choice == 3:
        while True:
            menu_choice = int(input(check_out_menu))

            # Print Room Status
            if menu_choice == 1:
                count = 0
                for location in hotels:
                    for room_number in hotels[0].keys():
                        if hotels[count][room_number] == '':
                            print(f'{room_number} is vacant')
                        else:
                            print(f'{room_number} is occupied by {hotels[count][room_number]}')
                    count += 1

            #Check Out
            elif menu_choice == 2:
                room_number = input('Which Room Number? ')
                which_location = int(input('Which Location? '))
                check_out(room_number, which_location)

            #exit
            elif menu_choice == 3:
                break


    # 4. Admin Features Menu
    elif menu_choice == 4:
        while True:
            menu_choice = int(input(admin_menu))

            # Print Guest List
            if menu_choice == 1:
                print(guests)
            
            # Save Hotel Info
            # Would like to save both the hotels var and the guests var to the same JSON file ???????????
            elif menu_choice == 2:
                import json
                file_name = 'hotel_list.json'

                with open(file_name, 'w') as file_to_save:
                    json.dump(hotels, file_to_save)
                print('The file has been saved')

            # Load Hotel Info
            elif menu_choice == 3:
                print(hotels)
                temp = input('What file would you like to import? ')
                import json
                file_name = temp

                with open(file_name, 'r') as file_to_load:
                    hotels = json.load(file_to_load)
                print('The file has been loaded')
                print(hotels)


            # Is room vacant
            elif menu_choice == 4:
                location = int(input('Which Location? '))
                room_number = input('Which Room Number? ')
                is_vacant(location, room_number)

            elif menu_choice == 5:
                break


    # 5. Exit
    elif menu_choice == 5:
        print('Thank You')
        break























####### Why does one work and not the other
                # count = 0
                # while count < len(hotels):
                #     name = hotels[0]["name"]
                #     print(name)
                #     count += 1

                # count = 0
                # while count < len(hotels):
                #     name = hotels[count]["name"]
                #     print(name)
                #     count += 1