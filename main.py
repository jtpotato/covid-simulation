from find_r0 import *
from simulation import *
# Find the r0 of COVID using data from March 1st to 6th July 2020.

initial_cases_cumulative = 282
final_cases_cumulative = 9826
days = 10 # Days between 21-01-2020 and 31-01-2020

covid_r0 = find_r0(initial_cases=initial_cases_cumulative, final_cases=final_cases_cumulative, days=days, iterations=10000)
print(f"COVID R0: {covid_r0}")

# Simulate the spread of COVID in the world, from 100 cases over 365 days.
simulate(population=8000000000, initial_cases=100, simulation_days=365, covid_r0=covid_r0, immune_days=200, save_file=True, filename="data/no_intervention.csv")