# from Animals.Bird import Bird
from operator import attrgetter


class BirdManager:
    def __init__(self, all_animals=[]):
        self.all_birds = all_animals
        self.search_results = []

    def search_birds(self, list_of_animals: list):
        for i in list_of_animals:
            if i.animal_type == "Bird":
                self.all_birds.append(i)

    def sort_by_mass(self, all_birds: list = None, is_reversed=False):
        if all_birds is None:
            self.all_birds.sort(key=attrgetter("mass_in_kg"), reverse=is_reversed)
            result = self.all_birds
        else:
            all_birds.sort(key=attrgetter("mass_in_kg"), reverse=is_reversed)
            result = all_birds
        return result

    def sort_by_feed(self, all_birds: list = None, is_reversed=False):
        if all_birds is None:
            self.all_birds.sort(key=attrgetter("feed_per_day_in_kg"), reverse=is_reversed)
            result = self.all_birds
        else:
            all_birds.sort(key=attrgetter("feed_per_day_in_kg"), reverse=is_reversed)
            result = all_birds
        return result

    def search_by_migratory(self, is_sort_by_mass=True, is_reversed=False):
        for i in self.all_birds:
            if i.is_migratory is True:
                self.search_results.append(i)
        if is_sort_by_mass is True:
            self.sort_by_mass(self.search_results, is_reversed)
        else:
            self.sort_by_feed(self.search_results, is_reversed)
        return self.search_results

#    @property
#   def all_birds(self):
#        return self._all_birds

#    @property
#    def search_results(self):
#        return self._search_results
