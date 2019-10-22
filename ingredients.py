'''
Ingredient Generators
'''

from data import WordPickFile, WordPick, SentenceGenerator

Animal = WordPickFile("data/animal.txt")
Common = WordPickFile("data/common.txt")
Mineral = WordPickFile("data/mineral.txt")
Plant = WordPickFile("data/plant.txt")
Substance = WordPickFile("data/substance.txt")

# (Crushed | Powdered | ...) Mineral
Processing = WordPick(["Crushed", "Powdered", "Ground", "Distilled"])
ReducedMineral = SentenceGenerator([Processing, Mineral])

# Substance (dews etc)
SubstanceDew = SentenceGenerator(["A drop of", Substance])

# (Blood | Spit | ...) of Animal
AnimalBit = WordPick(["Blood", "Spit", "Bone"])
AnimalPart = SentenceGenerator([AnimalBit, "of", Animal])

# Latin name of plant
LatinPlant = SentenceGenerator([Plant])

# Various common ingredients, such as basic berries or herbs
CommonIngredient = SentenceGenerator([Common])

ingredients = [ReducedMineral, SubstanceDew, AnimalPart, LatinPlant, CommonIngredient]