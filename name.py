'''
Potion Name Generator
'''

from data import WordPickFile, SentenceGenerator

Ailments = WordPickFile("data/ailment.txt")
Effect = WordPickFile("data/effect.txt")
Wizard = WordPickFile("data/wizard.txt")

# Potion of Effect
StandardPotion = SentenceGenerator(["Potion of", Effect])

# Wizard Name's Potion
WizardPotion = SentenceGenerator([Wizard, "Potion"])

# Wizard Name's Potion of Effect
WizardPotionEffect = SentenceGenerator([Wizard, "Potion of", Effect])

# Ailment Remover
AilmentRemover = SentenceGenerator([Ailments, "Remover"])

names = [StandardPotion, WizardPotion, WizardPotionEffect, AilmentRemover]