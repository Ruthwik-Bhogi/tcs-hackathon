import random

class HospitalTwin:

    def __init__(self):
        self.er = 20
        self.icu = 8
        self.general = 30

    def step(self):

        # patient inflow variation
        self.er += random.randint(-2, 5)
        self.icu += random.randint(-1, 2)
        self.general += random.randint(-3, 3)

        # constraints
        self.er = max(0, self.er)
        self.icu = max(0, self.icu)
        self.general = max(0, self.general)

        total = self.er + self.icu + self.general

        return {
            "er": self.er,
            "icu": self.icu,
            "general": self.general,
            "total": total
        }
