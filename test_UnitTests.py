import unittest
from Manager.BirdManager import BirdManager
from Animals.Parrot import Parrot
from Animals.Pelican import Pelican
from operator import attrgetter
from Enums.Feed import Feed


class TestBirdManager(unittest.TestCase):
    def setUp(self):
        self.all_animal_test_list = \
            [
                Parrot(species="Watermelon", mass_in_kg=12, feed_per_day_in_kg=1.5,
                       type_of_feed=Feed.CORN, age_in_years=6,
                       is_migratory=False, size_of_wings_in_cm=50),
                Parrot(species="Rainbow Coloured", mass_in_kg=9, feed_per_day_in_kg=1,
                       type_of_feed=Feed.CORN, age_in_years=7,
                       is_migratory=False, size_of_wings_in_cm=42),
                Pelican(species="Marine", mass_in_kg=20, feed_per_day_in_kg=3,
                        type_of_feed=Feed.FISH, age_in_years=13,
                        is_migratory=True, size_of_wings_in_cm=65),
                Pelican(species="Boba", mass_in_kg=17, feed_per_day_in_kg=2.7,
                        type_of_feed=Feed.FISH, age_in_years=10,
                        is_migratory=True, size_of_wings_in_cm=68)]
        self.bird_manager = BirdManager(self.all_animal_test_list)

    def test_search_birds(self):
        expected_result = self.all_animal_test_list.copy()
        self.assertEqual(expected_result, self.all_animal_test_list)

    def test_sort_by_mass(self):
        expected_result = self.all_animal_test_list.copy()
        expected_result.sort(key=attrgetter("mass_in_kg"), reverse=False)
        self.assertEqual(expected_result, self.bird_manager.sort_by_mass(is_reversed=False))
        self.assertEqual(expected_result, self.bird_manager.sort_by_mass(self.bird_manager.all_birds,
                                                                         is_reversed=False))
        expected_result.sort(key=attrgetter("mass_in_kg"), reverse=True)
        self.assertEqual(expected_result, self.bird_manager.sort_by_mass(is_reversed=True))
        self.assertEqual(expected_result, self.bird_manager.sort_by_mass(self.bird_manager.all_birds,
                                                                         is_reversed=True))

    def test_sort_by_feed(self):
        expected_result = self.all_animal_test_list.copy()
        expected_result.sort(key=attrgetter("feed_per_day_in_kg"), reverse=False)
        self.assertEqual(expected_result, self.bird_manager.sort_by_feed(is_reversed=False))
        self.assertEqual(expected_result, self.bird_manager.sort_by_feed(self.bird_manager.all_birds,
                                                                         is_reversed=False))
        expected_result.sort(key=attrgetter("feed_per_day_in_kg"), reverse=True)
        self.assertEqual(expected_result, self.bird_manager.sort_by_feed(is_reversed=True))
        self.assertEqual(expected_result, self.bird_manager.sort_by_feed(self.bird_manager.all_birds,
                                                                         is_reversed=True))

    def test_search_by_migratory(self):
        expected_result = []
        for i in self.all_animal_test_list:
            if i.is_migratory is True:
                expected_result.append(i)
        expected_result.sort(key=attrgetter("mass_in_kg"), reverse=False)
        self.assertCountEqual(self.bird_manager.search_by_migratory(True, False), expected_result)
        expected_result.sort(key=attrgetter("mass_in_kg"), reverse=True)
        self.assertCountEqual(self.bird_manager.search_by_migratory(True, True), expected_result)
        expected_result.sort(key=attrgetter("feed_per_day_in_kg"), reverse=False)
        self.assertCountEqual(self.bird_manager.search_by_migratory(False, False), expected_result)
        expected_result.sort(key=attrgetter("feed_per_day_in_kg"), reverse=True)
        self.assertCountEqual(self.bird_manager.search_by_migratory(False, True), expected_result)

