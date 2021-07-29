from pprint import pprint
import os




def recipe_dict():
    folder_path = os.getcwd()
    path = f"{folder_path}/recipes.txt"
    cook_book = {}
    with open(path,"r", encoding='utf-8') as file:
        for line in file:
            dish = line.strip()
            ingredients_quantity = int(file.readline().strip())

            ingredients_list = []
            for ingredient in range(ingredients_quantity):
                dict_ingredient = dict()
                ingredient_name, quantity, measure = file.readline().strip().split(" | ")
                dict_ingredient['ingredient_name'] = ingredient_name
                dict_ingredient['quantity'] = quantity
                dict_ingredient['measure'] = measure
                ingredients_list.append(dict_ingredient)

            file.readline()
            cook_book[dish] = ingredients_list

    return cook_book

def get_shop_list_by_dishes(dishes, quantity_person):
    cook_book = recipe_dict()
    amount_of_ingredients_for_dishes = dict()
    for dish in dishes:
        for dish_names, ingredients in cook_book.items():
            for ingredient_and_msr_quantity in ingredients:
                if dish == dish_names:
                    ingredient_name = ingredient_and_msr_quantity['ingredient_name']
                    if ingredient_name not in amount_of_ingredients_for_dishes.keys():
                        amount_of_ingredients_for_dishes[ingredient_name] = {
                            'measure': ingredient_and_msr_quantity['measure'],
                            'quantity': int(ingredient_and_msr_quantity['quantity']) * quantity_person}
                    else:
                        amount_of_ingredients_for_dishes[ingredient_name] = {
                            'measure': ingredient_and_msr_quantity['measure'],
                            'quantity': ((int(ingredient_and_msr_quantity['quantity'])) +
                                         (int(ingredient_and_msr_quantity['quantity']))) * quantity_person}

    pprint(amount_of_ingredients_for_dishes)

def longer_length():
    folder_path_1txt = os.getcwd()
    path_1txt = f"{folder_path_1txt}/1.txt"
    folder_path_2txt = os.getcwd()
    path_2txt = f"{folder_path_2txt}/2.txt"
    folder_path_3txt = os.getcwd()
    path_3txt = f"{folder_path_3txt}/3.txt"
    with open(path_1txt, "r", encoding="utf-8") as file:
        text_1txt = file.readlines()
        len_1txt = len(text_1txt)

    with open(path_2txt, "r", encoding="utf-8") as file:
        text_2txt = file.readlines()
        len_2txt = len(text_2txt)

    with open(path_3txt, "r", encoding="utf-8") as file:
        text_3txt = file.readlines()
        len_3txt = len(text_3txt)

    if len_3txt > len_2txt > len_1txt:
        print("3.txt")
        print(' '.join(text_3txt))
        print("2.txt")
        print(' '.join(text_2txt))
        print("1.txt")
        print(' '.join(text_1txt))
    elif len_3txt > len_1txt > len_2txt:
        print("3.txt")
        print(' '.join(text_3txt))
        print("1.txt")
        print(' '.join(text_1txt))
        print("2.txt")
        print(' '.join(text_2txt))
    elif len_2txt > len_3txt > len_1txt:
        print("2.txt")
        print(' '.join(text_2txt))
        print("3.txt")
        print(' '.join(text_3txt))
        print("1.txt")
        print(' '.join(text_1txt))
    elif len_2txt > len_1txt > len_3txt:
        print("2.txt")
        print(' '.join(text_2txt))
        print("1.txt")
        print(' '.join(text_1txt))
        print("3.txt")
        print(' '.join(text_3txt))
    elif len_1txt > len_3txt > len_2txt:
        print("1.txt")
        print(' '.join(text_1txt))
        print("3.txt")
        print(' '.join(text_3txt))
        print("2.txt")
        print(' '.join(text_2txt))
    elif len_1txt > len_2txt > len_3txt:
        print("1.txt")
        print(' '.join(text_1txt))
        print("2.txt")
        print(' '.join(text_2txt))
        print("3.txt")
        print(' '.join(text_3txt))






pprint(recipe_dict())
print()
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
print()
longer_length()






