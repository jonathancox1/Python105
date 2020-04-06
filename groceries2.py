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

main_menu = '''

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

1. Print List
2. Edit Single Item
3. Edit Multiple Items
4. Return Home

'''
#REMOVE ITEMS
remove_items_sub_menu = '''

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
        
    # 2. Add Items
    elif menu_choice == 2:
        # Displays submenu
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
        # Displays submenu
        edit_items_choice = int(input(add_items_sub_menu))
        # Displays List
        if edit_items_choice == 1:
            for i in range(len(groceries)):
                print(f'{i} - {groceries[i]}')
        # Edits a Single Item
        elif edit_items_choice == 2:
            pass
        # Edits Multiple Items
        elif edit_items_choice == 3:
            pass
        # Return Home
        elif edit_items_choice == 4:
            pass 
    
    # 4. Remove Items - brings up submenu
    elif menu_choice == 4:
        # Displays submenu
        remove_item_choice = int(input(add_items_sub_menu))
        # Displays List
        if remove_item_choice == 1:
            for i in range(len(groceries)):
                print(f'{i} - {groceries[i]}')
        # Remove a Single Item
        elif remove_item_choice == 2:
            pass
        # Remove Multiple Items
        elif remove_item_choice == 3:
            pass
        # Print Removed Items List
        elif remove_item_choice == 4:
            pass
        # Return Home
        elif remove_item_choice == 5:
            pass

    # 5. Quit - exits program     
    else:
        print('Thank you for using the grocery list app!')
        break

