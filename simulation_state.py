import random


class Simulation:
    city_populations = [random.randint(100000, 2000000) for _ in range(10)]
    city_infected = [0 for _ in range(10)]
    city_commute_intake = [0 for _ in range(10)]

    def print_state(self):
        for i in range(len(self.city_populations)):
            print(f"City {i+1}: {self.city_populations[i]} people, {self.city_infected[i]} infected, {self.city_commute_intake[i]} infected commuting to this city.")

        print()