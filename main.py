def open_cook_book (file):
    with open(file, encoding='utf-8') as recipe:
        cook_book = {}
        for element in recipe:
            dish = element.strip()
            quantity = int(recipe.readline().strip())
            result = []
            for product in range(quantity):
                data = {}
                line = recipe.readline().split('|')
                data['ingredient_name'] = line[0].strip()
                data['quantity'] = line[1].strip()
                data['measure'] = line[2].strip()
                result.append(data)
            cook_book[dish] = result
            recipe.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    products = []
    for dish in dishes:
        if dish in cook_book.keys():
            products.append(cook_book[dish])
    product = []
    for i in products:
        for x in range(len(i)):
            product.append(i[x])
    result = {}
    for item in product:
        qwe = {}
        qwe['measure'], qwe['quantity'] = item['measure'], item['quantity']
        if item['ingredient_name'] not in result.keys():
            result[item['ingredient_name']] = qwe
        else:
            qwe['quantity'] = (int(result[item['ingredient_name']]['quantity']) + int(item['quantity']))
            result[item['ingredient_name']] = qwe
    for i in result:
        result[i]['quantity'] = int(result[i]['quantity'])*person_count
    return result


file = 'recipe_book.txt'
cook_book = open_cook_book(file)
list_of_ingredients = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос', 'Фахитос', 'Фахитос'], 10)
print(list_of_ingredients)