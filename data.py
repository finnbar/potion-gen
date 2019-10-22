from random import choice

def importData(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip() for x in content]

class Picks:
    def __init__(self):
        self.choices = []

    def choose(self):
        return choice(self.choices)

class WordPickFile(Picks):
    def __init__(self, filename):
        self.choices = importData(filename)    

class WordPick(Picks):
    def __init__(self, words):
        self.choices = words

class SentenceGenerator:
    def __init__(self, components):
        self.components = components

    def create(self):
        def resolve(part):
            if isinstance(part, Picks):
                return part.choose()
            else: return part

        return " ".join(list(map(resolve, self.components)))