import csv
import random


def add_recipe():

    ''' 
    This function is responsible for adding new recipes to the csv file.
    It stores the user inputs on the empty dictionary "recipes" and when user finishes adding items it will loop thru "recipes" and write everything to the csv.
    '''

    recipes = {}

    while True:
        recipe_name = input("Enter the name of the recipe to save: ")
        recipe_items = input("Now enter the ingredients, separated by a comma (,). Press Enter to finish. ").split(",")
        recipe_items = [ingredients.lower().strip() for ingredients in recipe_items] #this makes all the ingredients given by the user lower case and strips of spaces before and after the words
                                                                                     #this way it will be easier to later search for ingredients
        recipes[recipe_name] = recipe_items  #this is when the dictionary gets the new recipe name added, and then it adds every ingredient to that name

        cont = input("Want to add another recipe? (y/n) ")
        if cont == "n":
            with open('recipes.csv', 'a') as f:                                     #opens the csv file, if none exists with this name, a new one will be created
                for recipe_name in recipes.keys():                                  # loops thru every "recipe_name" from the "recipes" dictionary
                    f.write("%s, %s\n" % (recipe_name, recipes[recipe_name]))       #writing every row of data into the csv file
            break
   
def pick_random_recipe():

    ''' 
    This function is responsible for picking a random recipe from the entire dictionary stored in the csv file
    '''

    with open('recipes.csv', 'r') as recipes:                      #this opens the file so we can read and use the data stored inside
        recipe_reader = csv.reader(recipes)                        #the file data is saved to a variable so from here we're working with the data inside the variable, which is a copy of the csv file
        recipe_dict = {}                                           #the data inside the variable needs to be writed from the "recipe_reader" into this dictionary "recipe_dict"
        for row in recipe_reader:                                  
            recipe_dict[row[0]] = {'ingredients':row[1:]}          #loop writing every row of data into the empty "recipe_dict" dictionary
        recipe_picked = random.choice(list(recipe_dict.keys()))    #picking a random key, in this case a recipe_name using the random module. The recipe_dict needs to be passed as a list because we can't use random module on a dictionary
        print("Try the recipe: " + str(recipe_picked))             #prints the random recipe chosen
        print("This are the ingredients of the recipe " + str(recipe_dict[recipe_picked]['ingredients'])) #finds the ingredients for the recipe that was chosen an prints it to help the user make the recipe

def pick_recipe_by_ingredient(ing_choice):

    ''' 
    This function is responsible for searching for recipes with the ingredient given by the user, then picking a random one from those found.
    The function receives one input from the "main" function, that being the ingredient the user picked, that we will use to search for matches
    '''

    with open('recipes.csv', 'r') as recipes:                    #same steps as with the "pick_random_recipe" function, to open and store the data inside the csv file to a new dictionary
        recipe_reader = csv.reader(recipes)
        recipe_list = {}
        recipes_with_user_ingredient = []                        #creates a empty list were we will store the names of the recipes that have the ingredient that the user wants
        for row in recipe_reader:
            recipe_list[row[0]] = {'ingredients':row[1:]}
        
        for recipe_name in recipe_list.keys():                                #this loop will look thru every key in the data, open it and then open its list of ingredients
            ingredient_finder = recipe_list[recipe_name]['ingredients']       #saving the path to the ingredients list to a variable so its easier to call
            for i in range((len(ingredient_finder))):                         
                if ing_choice in ingredient_finder[i]:                     #will loop thru the ingredients of every recipe and if there is a match will append the recipe to our empty list
                    recipes_with_user_ingredient.append([recipe_name])
        if (len(recipes_with_user_ingredient)) == 0:                          #handles the case where there is no recipe with that ingredient
            print('Sorry, there is no recipe with that ingredient, try adding one for next time')
        else:                                                                 #when there is matches, it will pick one at random, and once again give that name and the full list of ingredients
            recipe_generated = random.choice(recipes_with_user_ingredient)
            print('How about cooking the recipe: ' + str(recipe_generated[0]))
            print('This are the ingredients of the recipe ' + str(recipe_list[recipe_generated[0]]['ingredients']))
                
def main():

    ''' 
    This is the main function, where it will check for the user inputs and navigate thru the menus
    '''

    while True:
        user_choice = input("Press 1 to pick a recipe, press 2 to add a new recipe to the database. Enter to quit. ") #this is the main menu for the program, user can pick where to go
        if user_choice == '1':
            ing_choice = input("Write 'random' for a random recipe from the database, \nWrite the desired ingredient (ex:'chicken') to get a recipe with that ingredient: ").lower().strip() # strips of spaces and sets to lower case so we don't encounter errors in the search by ingredient
            if ing_choice == 'random':
                pick_random_recipe()
                break
            else:
                pick_recipe_by_ingredient(ing_choice)
                break
        elif user_choice == '2':          #we don't break after add_recipe so the user can add multiple recipes without needing to relaunch the program
            add_recipe()               
        elif user_choice == "":
            break
        else:
            while user_choice != '1' or user_choice != '2':                   #handling the case where the user doesn't press 1 or 2
                user_choice = input("You did not give a valid input! Try again or press Enter to quit. ")
                if user_choice == '1':
                    ing_choice = input("Write 'random' for a random recipe from the database \nWrite the desired ingredient (ex:'chicken') to get a recipe with that ingredient: ")
                    if ing_choice == 'random':
                        pick_random_recipe()
                        break
                    else:
                        pick_recipe_by_ingredient(ing_choice)
                        break
                elif user_choice == '2':
                    add_recipe()
                elif user_choice == "":
                    break

if __name__ == '__main__':
    main()