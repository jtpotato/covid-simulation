import random
from implement_policy import ImplementPolicy

class City:
    population = 0
    cases = []
    day = 0
    case_history = []
    recovered = 0
    policy = ImplementPolicy()

    def __init__(self, population, cases):
        self.population = population
        self.cases = [cases]
        self.case_history = [cases]

    def add_cases(self, cases):
        self.cases.append(cases)
        self.case_history.append(cases)
        # Assume 10 day infections.
        if len(self.cases) > 10:
            self.recovered += self.cases.pop(0)


    def get_total_cases(self):
        return sum(self.cases)
    
    def simulate_day_small(self):
        new_cases_today = 0
        for i in range(self.get_total_cases()):
            for j in range(self.policy.people_met): # Assumption: people meet 20 people every day.
                if random.random() < self.policy.infection_chance:
                    new_cases_today += 1

        self.add_cases(new_cases_today)

    def simulate_day(self):
        if self.get_total_cases() < 50:
            self.simulate_day_small()
        else:
            potential_infections = self.get_total_cases() * self.policy.infection_chance * self.policy.people_met
            # how many of those potential infections are actually able to be infected?
            able_to_be_infected = 0
            if self.policy.reinfections:
                able_to_be_infected = 1 - (self.get_total_cases() / self.population)
            else:
                able_to_be_infected = 1 - ((self.get_total_cases() + self.recovered) / self.population)
            self.add_cases(int(potential_infections * able_to_be_infected))

        

        self.day += 1