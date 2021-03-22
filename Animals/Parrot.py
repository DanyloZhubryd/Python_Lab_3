from Animals.Bird import Bird


class Parrot(Bird):
    def __init__(self, species="", mass_in_kg=0, feed_per_day_in_kg=0,
                 type_of_feed=None, age_in_years=0,
                 is_migratory=None, size_of_wings_in_cm=0):
        super(Parrot, self).__init__(species, mass_in_kg, feed_per_day_in_kg,
                                     type_of_feed, age_in_years,
                                     is_migratory, size_of_wings_in_cm)

    def talk(self, speech=""):
        return "{species} says {speech}".format(species=self.species, speech=speech)

    def __repr__(self):
        return "\nParrot: {mass}, {talk}".format(mass=self.mass_in_kg, talk=self.talk("HI THERE"))
