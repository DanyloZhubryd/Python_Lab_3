from Animals.Animal import Animal


class Bird(Animal):
    def __init__(self, species="", mass_in_kg=0, feed_per_day_in_kg=0,
                 type_of_feed=None, age_in_years=0,
                 is_migratory=None, size_of_wings_in_cm=0):
        super(Bird, self).__init__(species, mass_in_kg, feed_per_day_in_kg,
                                   type_of_feed, age_in_years)
        self._animal_type = "Bird"
        self._is_migratory = is_migratory
        self._size_of_wings_in_cm = size_of_wings_in_cm

    @property
    def is_migratory(self):
        return self._is_migratory

    @property
    def size_of_wings_in_cm(self):
        return self._size_of_wings_in_cm

    @property
    def animal_type(self):
        return self._animal_type
