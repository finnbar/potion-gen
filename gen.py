'''
Utilises the ingredient generators to build actual recipes.
Also uses the name generators to build a name.
'''

from random import choice, randrange
from ingredients import ingredients
from name import names

def generatePotion():
    ingredientCount = randrange(4, 7)
    recipeIngredients = []
    while len(recipeIngredients) < ingredientCount:
        newIngredient = choice(ingredients).create()
        if not newIngredient in recipeIngredients:
            recipeIngredients.append(newIngredient)
    name = choice(names).create()
    return name + ":\n" + "\n".join(recipeIngredients)

if __name__ == '__main__':
    for i in range(10):
        print(generatePotion())
        print("\n")