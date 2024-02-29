import ipdb
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    heat_level_emoji = '🌶' * 8
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji[:food['heat_level']]}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food['cuisine'] == cuisine), None)

def print_spiciest_foods(spicy_foods):
    filtered_spicy_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    heat_level_emoji = '🌶' * 8
    for food in filtered_spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoji[:food['heat_level']]}")

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_spicy_foods = 0
    for food in spicy_foods:
        total_heat_level += food['heat_level']
        num_spicy_foods += 1
    return total_heat_level//num_spicy_foods if num_spicy_foods > 0 else 0    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
