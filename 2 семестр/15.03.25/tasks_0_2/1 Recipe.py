class Recipe:
    def __init__(self, *args):
        self.recipe = []
        if args:
            for i in args:
                self.recipe.append(i)
    
    def add_ingredient(self, ing):
        self.recipe.append(ing)
    
    def remove_ingredient(self, ing):
        self.recipe.remove(ing)
    
    def get_ingredients(self):
        # get = []
        # for i in self.recipe:
        #     get.append(str(i))
        # get = tuple(get)
        get = tuple(self.recipe)
        return get

    def __len__(self):
        return len(self.recipe)


class Ingredient:
    def __init__(self, name_, volume_, measure_):
        self.name = name_
        self.volume = volume_
        self.measure = measure_

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


# ing1 = Ingredient('Соль', 1, 'столовая ложка')
# ing2 = Ingredient('Мясо', 5, 'столовая вилка')
# ing3 = Ingredient('Икра', 1, 'столовая линейка')
# recipe1 = Recipe(ing1, ing2)
# print(recipe1.get_ingredients())
