from functions.list_functions import create_list_item as create_shopping_item

shopping_list = []

shopping_list.append(create_shopping_item('food', 'spaghetti', '2'))
shopping_list.append(create_shopping_item('supplies', 'pens', '4'))

print(shopping_list)