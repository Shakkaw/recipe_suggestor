import csv
import random


def add_recipe():
        
    recipes = {}

    while True:
        recipe_name = input("Enter the name of the recipe to save: ")
        recipe_items = input("Now enter the ingredients, separated by a comma (,). Press Enter to finish. ").split(",")
        recipe_items = [ingredients.lower().strip() for ingredients in recipe_items]

        recipes[recipe_name] = recipe_items

        cont = input("Want to add another recipe? (y/n) ")
        if cont == "n":
            with open('recipes.csv', 'a') as f:
                for key in recipes.keys():
                    f.write("%s, %s\n" % (key, recipes[key]))
            break
   
def pick_random_recipe():

    with open('recipes.csv', 'r') as recipes:
        recipe_reader = csv.reader(recipes)
        recipe_list = {}
        for row in recipe_reader:
            recipe_list[row[0]] = {'ingredients':row[1:]}
        recipe_picked = random.choice(list(recipe_list.keys()))
        print("Try the recipe: " + str(recipe_picked))
        print("This are the ingredients of the recipe " + str(recipe_list[recipe_picked]['ingredients']))

def pick_recipe_by_ingredient(recipe_choice):
    with open('recipes.csv', 'r') as recipes:
        recipe_reader = csv.reader(recipes)
        recipe_list = {}
        recipes_with_user_ingredient = []
        for row in recipe_reader:
            recipe_list[row[0]] = {'ingredients':row[1:]}
        
        for recipe_name in recipe_list.keys():
            ingredient_finder = recipe_list[recipe_name]['ingredients']
            for i in range((len(ingredient_finder))):
                  if recipe_choice in ingredient_finder[i]:
                      recipes_with_user_ingredient.append([recipe_name])
        recipe_generated = random.choice(recipes_with_user_ingredient)
        print('How about cooking the recipe: ' + str(recipe_generated[0]))
        print('This are the ingredients of the recipe ' + str(recipe_list[recipe_generated[0]]['ingredients']))
                
def main():
    
    while True:
        user_choice = input("Press 1 to pick a recipe, press 2 to add a new recipe to the database. Enter to quit. ")
        if user_choice == '1':
            recipe_choice = input("Write 'random' for a random recipe from the database, \nWrite the desired ingredient (ex:'chicken') to get a recipe with that ingredient: ")
            if recipe_choice == 'random':
                pick_random_recipe()
                break
            else:
                pick_recipe_by_ingredient(recipe_choice)
                break
        elif user_choice == '2':
            add_recipe()
        elif user_choice == "":
            break
        else:
            while user_choice != '1' or user_choice != '2':
                user_choice = input("You did not give a valid input! Try again or press Enter to quit. ")
                if user_choice == '1':
                    recipe_choice = input("Write 'random' for a random recipe from the database \nWrite the desired ingredient (ex:'chicken') to get a recipe with that ingredient: ")
                    if recipe_choice == 'random':
                        pick_random_recipe()
                        break
                    else:
                        pick_recipe_by_ingredient(recipe_choice)
                        break
                elif user_choice == '2':
                    add_recipe()
                elif user_choice == "":
                    break

if __name__ == '__main__':
    main()