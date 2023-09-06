#Billy Boone
#cs150
#04/16
#This is a program that prompts user for integers and then allows
#the user to display integers from a menu

import math

user_list = []

def get_list_from_user():
    
    while True:
        num = input('Enter integer (q to quit):')

        if num == 'q':
            return True
        
        elif num.isdigit():  #check if input is integer and append to user_list
            
            num = int(num)
            user_list.append(num)

        else:
            print("Invalid input.")
    
    return False
    

def print_menu():
    print('MENU')
    print('n - Number of integers in list')
    print('u - unique integers')
    print('o - odd integers')
    print('e - Even integers')
    print('a - Add integers')
    print('q - Quit')
    print()
    return input('Choose an option:')
    

def print_list(user_list):
    print(sorted(list(set(user_list))))


def num_in_list(user_list):
    return len(user_list)


def odd_integers(user_list):
    return [num for num in user_list if num % 2 != 0]


def even_integers(user_list):
    return [num for num in user_list if num % 2 == 0]


def add_integers():
    user_list.append(int(input('Enter integer: ')))


# Get integers from user
while True:
    quit_flag = get_list_from_user()
    if quit_flag:
        break

# Main program loop
menu_choice = ''
while True:
    menu_choice = print_menu()

    if menu_choice == 'n':
        print(f'There are {num_in_list(user_list)} integers in the list.\n')
    elif menu_choice == 'u':
        print('Unique integers in the list:')
        print_list(user_list)
        print()
    elif menu_choice == 'o':
        print('Odd integers in the list:')
        print(odd_integers(user_list))
        print()
    elif menu_choice == 'e':
        print('Even integers in the list:')
        print(even_integers(user_list))
        print()
    elif menu_choice == 'a':
        add_integers()
    elif menu_choice == 'q':
        if input('Are you sure you want to quit? (y/n): ') == 'y':
            break
    else:
        print('Invalid option.\n')

print('Goodbye!')

