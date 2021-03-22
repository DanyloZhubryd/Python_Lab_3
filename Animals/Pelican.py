from Animals.Bird import Bird


class Pelican(Bird):
    def __init__(self, species="", mass_in_kg=0, feed_per_day_in_kg=0,
                 type_of_feed=None, age_in_years=0,
                 is_migratory=None, size_of_wings_in_cm=0):
        super(Pelican, self).__init__(species, mass_in_kg, feed_per_day_in_kg,
                                      type_of_feed, age_in_years,
                                      is_migratory, size_of_wings_in_cm)

    def swim(self):
        return "░░░░░░░░░░░░░░░░░░░▄▄▄▄▄▄░░\n\
░░░░░░░▄▀▀▀▄░░░░░▄██{name}█░░░\n\
░░░▄███▀▒◐▒▒▌░░░░█▀▀▀▀▀░░░░\n\
░░░░░░░▌▒▒▒▒▐░░░▐░░░░░░░░░░\n\
░░░░░░░▐▒▒▒▒▐░░░▐░░░░░░░░░░\n\
░░░░░░░▌▒▒▒▒▐▄▄▄▐░░░░░░░░░░\n\
░▀▄▄▄▄▄▌▒▒▒▒▒▒▒▒▌▄▄▄▄▄▄█▀▀ ░\n\
░░▀█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▀▒▒ ▒▒\n\
▒▒▒▀█▓▐○▌▓▐○▌▓▐○▌▓█▀▒▒▒\n\
▒▒▒▒▒▒▀█▓▓▓▓▓▓▓▓▓█▀▒▒▒▒▒\n\
▒▒▒▒▒▒▒▒▀▀▀▀▀▀▀▀▀▀▒▒▒▒▒▒▒".format(name=self.species)

    def __repr__(self):
        return "\nPelican:{mass}\n{swim}".format(mass=self.mass_in_kg, swim=self.swim())
