hotel_atlanta = {
        'name' : 'atlanta',
        'room_numbers' : '',
}
hotel_boston = {
        'name' : 'boston',
        'room_numbers' : '',
}
hotel_barcelona = {
        'name' : 'barcelona',
        'room_numbers' : '',
}

room_template = {
        '101' : '',
        '102' : '',
        '103' : '',
        '104' : '',
        '105' : '',
}

room_info = {
    'occupant' : '',
    'bed_type' : 'King Bed',
    'pet_friend' : 'Yes',
}

hotel_atlanta['room_numbers'] = room_template
hotel_boston['room_numbers'] = room_template
hotel_barcelona['room_numbers'] = room_template

hotel_atlanta['room_numbers']['101'] = room_info
hotel_boston['room_numbers']['102'] = room_info
hotel_barcelona['room_numbers']['103'] = room_info


hotel_atlanta['room_numbers']['101']['occupant'] = ''
hotel_boston['room_numbers']['102']['occupant'] = ''
hotel_barcelona['room_numbers']['103']['occupant'] = ''


hotels = [hotel_atlanta, hotel_boston, hotel_barcelona]

hotels[0]['room_numbers']['101']['occupant'] = 'Dale Coop'
# print(hotels[0]['room_numbers']['101']['occupant'])

for hotel in hotels:
    for room in hotel['room_numbers'].keys():
        if hotel["room_numbers"][room] == '':
            print(f'{hotel["name"]} : {room} : Is Vacant')           
        else:
            occupant = hotel["room_numbers"][room]["occupant"]
            print(f'{hotel["name"]} : {room} : {occupant}')
        # print(room)
        pass
        # print(hotels[index]['room_numbers']['101']['occupant'])




# count = 0
# for location in hotels:
#     for room_number in hotels[0].keys():
#         if hotels[count][room_number] == '':
#             print(f'{room_number} is vacant')
#         else:
#             print(f'{room_number} is occupied by {hotels[count][room_number]}')
#     count += 1