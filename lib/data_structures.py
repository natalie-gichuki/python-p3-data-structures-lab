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
#use list comprehension
# (for food in spicy_food) used to loop through all the spicy foods
# (food["name"]) for every food in the dictionary this grabs the value assosiated with the "name" key
def get_names(spicy_foods):
   return [food["name"] for food in spicy_foods]
   print (get_names(spicy_foods))
   pass



def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    print(get_spiciest_foods(spicy_foods))
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat ="🌶" * food["heat_level"]
        if food["heat_level"] > 5:
            print (f"{name} ({cuisine}) | Heat Level: {heat}")
    pass

def get_average_heat_level(spicy_foods):
    #get sum of spiciness
    total_spicy = sum(food["heat_level"] for food in spicy_foods)
    #get sum of spicy foods
    total_food = len(spicy_foods)
    #divide total spiciness over number of foods
    return total_spicy / total_food
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

spicy_food = {
    "name": "Pilau",
    "cuisine": "Kenya",
    "heat_level": 7,
}

updated_list = create_spicy_food(spicy_foods, spicy_food)
print (updated_list)