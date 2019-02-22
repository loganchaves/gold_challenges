class Menu: 

    def __init__(self, number, name, description, ingredients ):
        self.number = number
        self.name = name
        self.description = description
        self.ingredients = ingredients
    def __repr__(self):
        return f"{self.number} {self.name} {self.description} {self.ingredients}"
