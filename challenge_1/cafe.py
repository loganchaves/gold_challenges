import menu 

menu_list = []

def add_menu_item (number, name, description, ingredients):
    m = menu.Menu(number, name, description, ingredients)
    menu_list.append(m)

def show_item():
    return (menu_list)

def delete_item(number):
    for menu in menu_list:
        if number == menu.number:
            index = menu_list.index(menu)
            del menu_list[index]
            return True
            
    