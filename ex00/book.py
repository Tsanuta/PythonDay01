from recipe import Recipe
import datetime


class Book:
    def __init__(self, name, creation_date):
        self.name = name
        self.last_update = datetime.datetime.now()
        self.creation_date = creation_date
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for x in self.recipe_list:
            for recipe in self.recipe_list[x]:
                if (recipe.name == name):
                    print(str(recipe))
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for x in self.recipe_list[recipe_type]:
            print(x.name)
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            self.recipe_list[recipe.recipe_type].append(recipe)
        else:
            print("This is not a recipe")
        pass
