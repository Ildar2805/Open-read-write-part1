def cook_book():
    with open('Recipes.TXT', encoding='utf-8') as file:
        cook_book = {}
        sep_dishes = file.read().split('\n\n')
        for sep_dish in sep_dishes:
            name, count, *ingredients = sep_dish.split('\n')
            total = []
            for ingredient in ingredients:
                ingredient_name, quantity, measure = ingredient.split(' | ')
                total.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = total
    return cook_book
print(cook_book())

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            ingredient, quantity, measure = ingredients.values()
            if ingredient not in shop_list:
                shop_list[ingredient] = {'measure': measure, 'quantity': quantity * person_count}
            else:
                shop_list[ingredient]['quantity'] += quantity * person_count
    return shop_list

def shop_list():
    person_count = int(input('Введите количество персон: '))
    dishes = input('Введите блюда, которые нужно будет приготовить (через запятую): ').capitalize().split(', ')
    print(get_shop_list_by_dishes(dishes, person_count))

shop_list()