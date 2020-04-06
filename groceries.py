#prompt the user for single grocery item
#append it to the 'groceries' list
# grocery_list = []
# grocery_list.append(input('Add your item to the grocery list: '))
# print(grocery_list)

####################################################################

#then in an infinite WHILE loop, prompt the user for an item
#append the item to the list
#print the list after the item has been added
#to exit the loop user should press Ctrl-C
# grocery_list = []
# while True:
#     grocery_list.append(input('Add your item to the grocery list (to exit type Ctrl-C):  '))
#     print(grocery_list)

####################################################################

#convert infinite WHILE loop, prompting user for grocery items
#array should only accept 3 items
#combine these lists
#then allow the user to select a specific index and replace with a specific item
#then print the new, user updated list

# groceries1 = []
# while len(groceries1) < 3:
#     item = input('What do you need: ')
#     groceries1.append(item)
    
# groceries2 = []
# while len(groceries2) < 3:
#     item = input('What do you need: ')
#     groceries2.append(item)
    

# #combine the lists
# master_list = groceries1 + groceries2
# print(master_list)

# #prompt the user for the index of the item to replace
# #give the user a range of indexs to refer to
# # for i in range(len(master_list)):
# #     print(f'Index: {i} - {master_list[i]}')


# lenght_of_list = len(master_list)
# index_to_replace = int(input(f'Which index would you like to replace (0 - {lenght_of_list}): '))

# #adjusts users input of index to reflect actual zero'd index
# #prompt the user for the new item
# index_to_replace -= 1
# item_to_replace = input('What would you like to replace it with: ')
# master_list[index_to_replace] = item_to_replace

# #print the updated combined list
# print(master_list)

##################################################################

#prompt user to input until they enter empty string
groceries = []
while True:
    to_add = input('Add your item to the grocery list, or exit by adding nothing: ')
    if to_add == '': #alternatly if len(to_add) == 0
        break
    groceries.append(to_add)


#print the array along with corresponding index
for i in range(len(groceries)):
    print(f'{i}index : {groceries[i]}')


#give them a chance to replace stuff in the array
#prompt for a subset of items to replace
replace_this = input('Would you like to replace something? y/n ')
if replace_this == 'y':
    #ask what to replace
    # to_replace = input('What would you like to replace? ')
    #ask where to slice (starting point)
    starting_point = int(input('At what index would you like to begin slicing? '))
    #ask where to slice (ending point)
    ending_poing = int(input('At what index would you like to end the slice? '))
    #if starting slice is equal to ending slice
    #replace only that single index
    if starting_point == ending_poing:
        replace_with = input('What would you like to replace it with? ')
        groceries[starting_point] = replace_with
    #if starting slice is different than ending slice
    #create new array
    else:
        list = []
        items_to_replace = (ending_poing - starting_point)
        #show user how many items they will be replacing
        #loop through giving the user option to input while there are still items to replace

        while True:
            replace_with = input('What shall we replace it with? Or exit by adding nothing: ')
            if replace_with != '':
                list.append(replace_with)
            else:
                break
        groceries[starting_point : ending_poing] = list
for i in range(len(groceries)):
    print(f'{i} : {groceries[i]}')





##   I TEND TO WRITE if new_item != ''     ##   IS THERE ONE METHOD THAT IS BETTER THAN THE OTHER
# while True:
# if new_item == '':
#     break
# replacements.append(new_item)


# how to compare two lists
# a = ['one', 'two', 'three', 'four', 'five']
# b = ['two', 'two', 'three', 'five', 'five']

# for i in range(len(a)):
#     if a[i] == b[i]:
#         print('True')
#     else:
#         print('False')