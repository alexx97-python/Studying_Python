
input_ = "fruit_banana,vegetable_carrot,fruit_apple,canned_sardines,drink_juice,fruit_orange"
output = "fruit:apple,banana,orange\nmeat:\nother:juice,sardines\nvegetable:carrot"


def group_groceries(groceries):
    items = groceries.split(',')
    list_fruit = []
    list_others = []
    list_meat = []
    list_vegetable = []

    for item in items:
        category = item.split('_')
        key = category[0]
        if key == 'fruit':
            list_fruit.append(category[1])
        elif key == 'meat':
            list_meat.append(category[1])
        elif key == 'vegetable':
            list_vegetable.append(category[1])
        else:
            list_others.append(category[1])

    return f'fruit:{",".join(sorted(list_fruit))}\n' \
           f'meat:{",".join(sorted(list_meat))}\n' \
           f'other:{",".join(sorted(list_others))}\n' \
           f'vegetable:{",".join(sorted(list_vegetable))}'


print(group_groceries(input_))