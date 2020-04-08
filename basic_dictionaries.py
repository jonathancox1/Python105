# DONT RUN THIS CODE # 
# NOTE TAKING ONLY #
####################
# # Basic Dictionary formating
friend = {
    'name': 'Elliot Alderson',
    'cell': '8675309',
    'snack': ['popcorn', 'reeces pieces'],
    'cat': {'toys': 'this',
            'treats': 'this',
            'friends': 'these',
            }
}

# Loops through dictionary and prints each corresponding key:value pair
keys = ['name', 'snack', 'cell']
for key in keys:
    print(f'{key}: {friend[key]}')

### OR use dict .keys() function!!!!!! #######
for key in friend.keys():
    print(f'{key}: {friend[key]}')

print(friend.keys())
#returns dict_keys(['name', 'cell', 'snack'])

print(friend.get('cat'))
#returns None

print(friend.get('cat', 'Does not have a cat'))
#looks for Key: 'cat' if doesnt exist prints second argument # ONLY SEARCHES FOR KEYS, not Values
#basically a Try: Except: statment

print(friend.get('name', 'Does not have a name'))
#returns 'Elliot Alderson'

'cat' in friend
#returns False
#only looks at keys

if 'cat' in friend:
    print(f'{friend["name"]} has a cat!')
else:
    print(f'We should get {friend["name"]} a cat!')


#loops through friend[snacks]
snacks = friend['snack']
for snack in snacks:
    print(f'{friend["name"]} loves {snack}')


#how to access a nested list in the dictionary
#first accesses the 'snack' key, then 0 the first index of the Value : list
frist_snack = friend['snack'][0]
#returns 'popcorn'
second_snack = friend['snack'][1]
#returns 'reeces pieces'
# OR USE .get() function
first_snack = friend.get('snack')[0]
#returns 'popcorn'
second_snack = friend.get('snack')[1]
#repturns 'reeces pieces'


#to reassign the value for key 'cell'
friend['cell'] = 1234567

#to create a new key and value to the existing friend dict.
friend['cat'] = 'Mr Robot'




#access dict inside anther dict
print(friend['cat']['toys'])



#to access a dictionary value in list of dictionaries
friends = [friend1, friend2]
#looks at the first index in friends list
elliot = friends[0]
#prints the 'cat' key in the friend1 dictionary
print(elliot['cat'])


#add dictionaries into an ongoing list
list_of_dicts = []
list_of_dicts.append(a_new_dict)

#use everything you can use on lists on dictionaries
#.get() .pop() .remove() del



