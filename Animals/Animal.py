class Animal:
    def __init__(self, species="", mass_in_kg=0, feed_per_day_in_kg=0,
                 type_of_feed=None, age_in_years=0):
        self._species = species
        self._mass_in_kg = mass_in_kg
        self._feed_per_day_in_kg = feed_per_day_in_kg
        self._type_of_feed = type_of_feed
        self._age_in_years = age_in_years

    @property
    def species(self):
        return self._species

    @property
    def mass_in_kg(self):
        return self._mass_in_kg

    @property
    def feed_per_day_in_kg(self):
        return self._feed_per_day_in_kg

    @property
    def type_of_feed(self):
        return self._type_of_feed

    @property
    def age_in_years(self):
        return self._age_in_years

    @mass_in_kg.setter
    def mass_in_kg(self, new_mass):
        self._mass_in_kg = new_mass

    @species.setter
    def species(self, new_species):
        self._species = new_species
