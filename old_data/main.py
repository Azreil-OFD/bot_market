from Shop_v1_1 import *

s = input("Введите название категории: ")
for i in category().data_list:
    if i.title == s:
        print(products(cat_id= i.id))
        break