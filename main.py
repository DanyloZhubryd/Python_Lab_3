from Animals.Pelican import Pelican
from Animals.Parrot import Parrot
from Zoo.Zoo import Zoo
from Manager.BirdManager import BirdManager
from Enums.Feed import Feed


def main():
    pelican_1 = Pelican(species="Marine", mass_in_kg=18, age_in_years=2,
                        feed_per_day_in_kg=2, type_of_feed=Feed.MEAT,
                        size_of_wings_in_cm=48, is_migratory=True)
    parrot_1 = Parrot(species="Rainbow Coloured", mass_in_kg=6, age_in_years=3,
                      feed_per_day_in_kg=0.5, type_of_feed=Feed.CORN,
                      size_of_wings_in_cm=32, is_migratory=False)
    parrot_2 = Parrot(species="Watermelon", mass_in_kg=8, age_in_years=1,
                      feed_per_day_in_kg=0.4, type_of_feed=Feed.CORN,
                      size_of_wings_in_cm=25, is_migratory=True)
    new_york_zoo = Zoo(pelican_1, parrot_1, parrot_2)
    birds_calc = BirdManager(all_animals=new_york_zoo.all_animals)
    print(birds_calc.search_by_migratory(True, True))
    parrot_1.mass_in_kg = 700
    print("{mass}".format(parrot_1.mass_in_kg))


if __name__ == '__main__':
    main()
