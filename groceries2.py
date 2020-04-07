'''
Instrutions:


The starter code provides you with the main menu for a command-line
based grocery list application.

The user should be able to add, update, and remove items.

Small exercise ------------------------------------------------
Using this starter code, you're going to combine the pieces of code
you've written so far to create the functionality for each action (either 
adding, updating, or removing an item).

Each time the user adds, updates, or deletes an item, they should see the main menu again.

Medium exercise ------------------------------------------------
For each sub-menu, show the user another menu with choices for that section of the application.
For example, when Removing Items, show the user this menu:

1. Print items
2. Delete an item
3. Delete multiple items
4. Return to main menu

If they enter "2", prompt them for the index of the item to delete.
If they enter "3", prompt them for a start index and an end index for the slice to delete.

After deleting, show them the "delete" menu again.
To return to the main menu, the user needs to enter "4" at the prompt.

Large exercise ------------------------------------------------
Add a second array that stores whether or not each grocery list item has been obtained.
Every time you add or remove an item, you need to add to or remove from this second list.

Add an additional main menu option for changing the status of any grocery list item.

Update the "Print Items" output so that it shows whether or not an item has been obtained.
'''


groceries = ['some', 'things', 'in', 'here']
removed_items = []

main_menu = '''
---- Home Menu----
1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Exit

'''
#ADD ITEMS
add_items_sub_menu = '''
----Add Items Menu---
1. Print List
2. Add Single Item
3. Add Multiple Items
4. Return Home

'''
#EDIT ITEMS
edit_items_sub_menu = '''
---- Edit Items Menu---
1. Print List
2. Edit Single Item
3. Edit Multiple Items
4. Return Home

'''
#REMOVE ITEMS
remove_items_sub_menu = '''
---Remove Items Menu---
1. Print List
2. Remove Single Item
3. Remove Multiple Items
4. Print Removed Items List
5. Return Home

'''

while True:
    menu_choice = int(input(main_menu))

    # 1. Print List - displays current grocery list
    if menu_choice == 1:
        for i in range(len(groceries)):
            print(f'{i} - {groceries[i]}')
        
    # 2. Add Items - brings up submenu
    elif menu_choice == 2:
        # Displays submenu and keeps user in submenu until break is met
        while True:
            add_items_choice = int(input(add_items_sub_menu))
            # Displays List
            if add_items_choice == 1:
                print('The Current List:')
                for i in range(len(groceries)):
                    print(f'{i} - {groceries[i]}')
            # Add a Single Item
            elif add_items_choice == 2:
                item_to_add = input('What would you like to add? ')
                groceries.append(item_to_add)
            # Add Multiple Items
            elif add_items_choice == 3:
                # Create a temp list to add to
                list_to_add = []
                # Prompt user to add to the list until typing EXIT
                while True:
                    item_to_add = input('What would you like to add? or press ENTER to exit ')
                    if item_to_add != '':
                        list_to_add.append(item_to_add)
                    else:
                        break
                groceries += list_to_add 
            # Return Home
            else:
                break 

    # 3. Edit Items - brings up submenu
    elif menu_choice == 3:
        # Displays submenu and keeps user in submen until break is met
        while True:
            edit_items_choice = int(input(edit_items_sub_menu))
            # Displays List
            if edit_items_choice == 1:
                for i in range(len(groceries)):
                    print(f'{i} - {groceries[i]}')
            # Edits a Single Item
            elif edit_items_choice == 2:
                for i in range(len(groceries)):
                    print(f'{i} - {groceries[i]}')
                item_to_edit = int(input('Which item number would you like to edit? '))
                y_or_n = input(f'You\'ve selected \'{groceries[item_to_edit]}\' is this correct y/n ')
                if y_or_n != 'y':
                    break
                else:
                    edited_item = input('What shall we change it to? ')
                    groceries[item_to_edit] = edited_item
            # Edits Multiple Items
            elif edit_items_choice == 3:
                for i in range(len(groceries)):
                    print(f'{i} - {groceries[i]}')
                starting_item_to_edit = int(input('Which item number would you like to start editing at? '))
                ending_item_to_edit = int(input('Which item number would you like to end editing at? '))
                # Cycle through, prompting the user to make edits while in predefined Slice
                while starting_item_to_edit <= ending_item_to_edit:
                    edit_with = input(f'What shall we replace \'{groceries[starting_item_to_edit]}\' with? ')
                    groceries[starting_item_to_edit] = edit_with
                    starting_item_to_edit += 1
            # Return Home
            elif edit_items_choice == 4:
                break 
    
    # 4. Remove Items - brings up submenu
    elif menu_choice == 4:
        # Displays submenu and keeps user in submenu until break is met
        while True:
            remove_item_choice = int(input(remove_items_sub_menu))
            # Displays List
            if remove_item_choice == 1:
                for i in range(len(groceries)):
                    print(f'{i} - {groceries[i]}')
            # Remove a Single Item
            elif remove_item_choice == 2:
                for i in range(len(groceries)):
                    print(f'{i} - {groceries[i]}')
                item_to_remove = int(input('Which item number would you like to remove? '))
                y_or_n = input(f'You\'ve selected \'{groceries[item_to_remove]}\' is this correct y/n ')
                if y_or_n != 'y':
                    break
                else:
                    removed_items.append(groceries.pop(item_to_remove))
            # Remove Multiple Items
            elif remove_item_choice == 3:
                for i in range(len(groceries)):
                    print(f'{i} - {groceries[i]}')
                starting_item_to_remove = int(input('Which item number would you like to start removing at? '))
                #ending_item_to_remove = int(input('Which item number would you like to end removing at? '))
                # Cycle through, prompting the user to make edits while in predefined Slice


                while starting_item_to_remove <= len(groceries):
                    y_or_n = input(f'You\'ve selected \'{groceries[starting_item_to_remove]}\' Would you like to remove y/n')
                    if y_or_n != 'y':
                        break
                    else:
                        removed_items.append(groceries.pop(starting_item_to_remove))
                        
                    

            # Print Removed Items List
            elif remove_item_choice == 4:
                print('**Removed Items List**')
                for i in range(len(removed_items)):
                    print(f'{i} - {removed_items[i]}')
            # Return Home
            elif remove_item_choice == 5:
                break

    # 5. Quit - exits program     
    else:
        print('Thank you for using the grocery list app!')
        break

