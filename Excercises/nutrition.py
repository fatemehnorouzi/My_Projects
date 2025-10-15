item= input("Item: ")
item= item.lower()

fruit= {'apple': 130, 'avocado': 50, 'banana': 110, 'cantaloupe': 50, 'grapefruit': 60,
       'grapes': 90, 'honeydew melon': 50, 'sweet cherries': 100}

if item in fruit.keys():
    print(fruit[item])