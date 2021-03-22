from Animals.Animal import Animal


class Zoo:
    def __init__(self, *args: Animal):
        self.all_animals = list(args)
