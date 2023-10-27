from find_r0 import *
from simulation import *
# Find the r0 of COVID using data from March 1st to 6th July 2020.

initial_cases_cumulative = 282
final_cases_cumulative = 9826
days = 10 # Days between 21-01-2020 and 31-01-2020

covid_r0 = find_r0(initial_cases=initial_cases_cumulative, final_cases=final_cases_cumulative, population=8000000000, days=days, iterations=10000, mode="cumulative")
print(f"COVID R0: {covid_r0}")

# Simulate the spread of COVID in the world, from 282 cases on March 1st
simulate(population=8000000000, initial_cases=282, simulation_days=305, covid_r0=covid_r0, immune_days=200, save_file=True, filename="data/no_intervention.csv")

# Find Re of COVID-19 using data from Victorian restrictions (mask wearing + lockdown) between the dates of 1 August and 1 September 2020.
covid_re_mask = find_r0(initial_cases=5919, final_cases=2519, population=6681000, days=31, iterations=10000, mode="active")
print(f"COVID Re (with Victorian Stage 4 - 2020 Restrictions): {covid_re_mask}")

# Simulate the spread of COVID in the world from 282 cases on March 1st, if the world followed Victorian restrictions during that timeframe.
simulate(population=8000000000, initial_cases=282, simulation_days=305, covid_r0=covid_re_mask, immune_days=200, save_file=True, filename="data/stage_4-2020.csv")

# Find Re of COVID-19 using data from V