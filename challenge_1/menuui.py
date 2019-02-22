import cafe
while True:
    print('welcome')
    user_input = input( '1. Add a item\n' +
                        '2. View menu\n' 
                        '3. Delete item\n'+
                        '4. Exit\n')
    if user_input == '1':
        number = input('Enter number: ')
        name = input('Enter name: ')
        description = input('Enter desctription: ')
        ingredients = input('enter ingredients: ')
        cafe.add_menu_item(number, name, description,ingredients)
    elif user_input == '2':
        print(cafe.menu_list)
    
    elif user_input == '3':

        number = input('enter item to delete')
        cafe.delete_item(number)
      
    elif user_input == '4':
        exit(0)
