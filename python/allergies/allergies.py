class Allergies(object):

    def __init__(self, number):
        all_allergies = { 1:'eggs', 2: 'peanuts',4:'shellfish',8:'strawberries',16:'tomatoes',32:'chocolate',64:'pollen',128:'cats'}

        self.allergies = []
        for i in all_allergies.keys():
            if (number & i):
                self.allergies.append(all_allergies[i])

    def is_allergic_to(self, string):
        return string in self.allergies;

    @property
    def lst(self):
        return self.allergies
