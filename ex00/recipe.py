class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if (isinstance(name, str) and
                isinstance(cooking_lvl, int) and
                cooking_lvl in range(1, 6) and
                isinstance(cooking_time, int) and cooking_time >= 0 and
                isinstance(ingredients, list) and
                isinstance(description, str) and
                isinstance(recipe_type, str) and
                recipe_type in ("starter", "lunch", "dessert")):
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        else:
            print("ERROR")
            exit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        """Your code goes here"""
        txt = "Recipe for " + self.name + ":"
        txt += "\nIngredients list: " + str(self.ingredients)
        txt += "\nTo be eaten for " + self.recipe_type
        txt += "\nTakes " + str(self.cooking_time) + " minutes of cooking."
        return txt
