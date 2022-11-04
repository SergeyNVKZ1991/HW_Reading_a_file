from pprint import pprint
import os

# # # current = os.getcwd()
# # # folder_name1 = 'py-homework-basic-files'
# # # folder_name = '2.4.files'
# # file_name = 'recipes.txt'
# # # full_path = os.path.join(current, folder_name1, folder_name, file_name)

def recipes():
    with open('recipes.txt', 'rt', encoding='utf8') as file:
        cook_book = {}
        dish_list = []
        for l in file:
            dish_name = l.strip()
            ingredients_list = []
            dish = {dish_name: ingredients_list}
            dish_count = file.readline()
            for i in range(int(dish_count)):
                dsh = file.readline().strip().split(' | ')
                ingredients_list.append({'ingredient_name': dsh[0],
                                         'quantity': int(dsh[1]),
                                         'measure': dsh[2]})
                dish_list.append(dish)
            blank_line = file.readline()
            cook_book.update(dish)
    return cook_book
# pprint(recipes())

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in recipes():
            for loc in recipes()[dish]:
                person_q = int(loc['quantity']) * person_count
                dict_list = {loc['ingredient_name']: {'measure': loc['measure'], 'quantity': person_q}}
                shop_list.update(dict_list)
    return shop_list
# pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def rec_file():
    lin_1 = {}
    for file in os.listdir('sorted'):
        with open(os.path.join('sorted', file), encoding='utf-8') as f:
            text = f.readlines()
            text_ = "".join(text)
            len_ = len(text)
            lin_1[file] = (f'{len_}\n{text_}\n')

    lin_2 = {}
    for x in sorted(lin_1, key=lin_1.get):
        lin_2[x] = lin_1[x]
    text_dict = {}
    for key, value in lin_2.items():
        with open('all_file.txt', 'a', encoding='utf-8') as f:
            f.writelines(f'{key}\n{value}\n')

