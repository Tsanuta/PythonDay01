from book import Book
from recipe import Recipe
import datetime


salade = Recipe("salade", 1, 10, ["salade", "tomates",
                "vinaigre", "moutarde"], "", "starter")
tourte = Recipe("tourte", 5, 45, ["viande", "farine",
                "oeufs", "creme"], "", "lunch")
mousse = Recipe("mousse", 4, 45, ["oeufs", "chocolat",
                "sucre", "creme"], "", "dessert")
tarte = Recipe("tarte", 2, 50, ["oeufs", "chocolat",
               "sucre", "creme", "farine"], "", "dessert")
to_print = str(tourte)
print(to_print)

my_book = Book("Mybook", datetime.datetime.now())
my_book.add_recipe(tourte)
my_book.add_recipe(salade)
my_book.add_recipe(mousse)
my_book.add_recipe(tarte)
my_book.get_recipes_by_types('dessert')
my_book.get_recipe_by_name("tarte")
