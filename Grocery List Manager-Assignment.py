#Assignment: Grocery List Manager
#Program description: This Python program helps users manage a grocery list.
#The program is allow users to add items to the list, Remove itmes from the list and view the current grocery list.

#This is the current grocery list, use a list code to start this program
current_items = ["Milk","egg","beef","pork","black pepper","ketchup","tomato","patato"]
#These fuunctions are three basic command for user to use
#remove_item() should give user the ability to remove items from the grocery list.
#add_item() should give user the ability to add items on the grocery list
#display_list() should print out the current items in the list to user
def remove_item():
   display_list()
   remove_num = input("Please enter the item number that you want to remove : ")
   if remove_num != "":
       remove_num = int(remove_num)
       if remove_num >= 0 and remove_num < len(current_items):
           removed = current_items.pop(remove_num)
           print(removed + " has been removed.")
       else:
           print("Invalid number. Please try again.")
   else:
       print("Please enter a number.")
def add_item():
   item_added = input("Please enter the item you want to add to the list : ")
   current_items.append(item_added)
   print(item_added + " has been added.")
def display_list():
   print("The current grocery list has:")
   for item in current_items:
       print(str(current_items.index(item)) + ". " + item)
#Now is the menu choices procided to users
print("This is Grocery list manager menu.")
print("Please select an option to process your using")
menu_choice = int(input("Please enter 1 for display the current list of grocery ,2 for adding items on the grocery list, 3 for removing items on the grocery list and 4 for exit the menu: "))
while menu_choice != 4:
   if menu_choice == 1:
       display_list()
   elif menu_choice == 2:
       add_item()
   elif menu_choice == 3:
       remove_item()
   else:
       print("The input is invalid, Please try again")
   
   menu_choice = int(input("Enter 1 to display list, 2 to add item, 3 to remove item, or 4 to exit: "))

print("Program exited. Goodbye!")
