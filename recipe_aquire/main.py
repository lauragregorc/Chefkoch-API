from chefkoch import ChefKochAPI, DataParser
from datetime import date

if __name__ == '__main__':
    categories = ChefKochAPI.get_categories()

    for category in categories:
        print(str(category))


    excluded_categories = ['Getränke', 'Alkoholfrei', 'Longdrink', 'Kaffee, Tee  Kakao', 'Likör', 'Bowle', 'Cocktail', 'Punsch', 'Shake']
    for category in categories[0:]:
        if category.title not in excluded_categories:
            category_recipes = ChefKochAPI.parse_recipes(category)
            DataParser.write_recipes_to_json('recipes/' + str(date.today()) + "-category-" + category.title.replace(" ", "-").replace("/", "-"), category_recipes)