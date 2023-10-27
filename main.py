from find_r0 import *
from simulation import *
# Find the r0 of COVID using data from March 1st to 6th July 2020.

initial_cases = 87137
final_cases = 12741386
days = 127 # Days between 1-3-2020 and 6-7-2020

covid_r0 = find_r0(initial_cases=initial_cases, final_cases=final_cases, days=days, iterations=1000)
print(f"COVID R0: {covid_r0}") # COVID R0: 1.2919999999999678 (floating point problems?)

# Simulate the spread of COVID in the world, from 100 cases over 365 days.
simulate(population=8000000000, initial_cases=100, simulation_days=365, covid_r0=covid_r0, recovery_days=14, immune_days=200, save_file=True, filename="data/no_intervention.csv")

# Simulate the spread of COVID with masks.
# Cutting the R0 by 75% is a rough estimate of the effectiveness of masks.
# For simplicity, policies come into effect when 5% of the population is infected.
simulate(population=8000000000, initial_cases=100, simulation_days=365, covid_r0=covid_r0, recovery_days=14, immune_days=200, policies=["MASKS"],  save_file=True, filename="data/masks.csv")

# Simulate the spread of COVID with lockdown.
# Cutting the R0 by 90% is a rough estimate of the effectiveness of lockdown.
simulate(population=8000000000, initial_cases=100, simulation_days=365, covid_r0=covid_r0, recovery_days=14, immune_days=200, policies=["LOCKDOWN"], save_file=True, filename="data/lockdown.csv")

# Simulate the spread of COVID with masks and lockdown.
simulate(population=8000000000, initial_cases=100, simulation_days=365, covid_r0=covid_r0, recovery_days=14, immune_days=200, policies=["MASKS", "LOCKDOWN"], save_file=True, filename="data/masks_and_lockdown.csv")

# Simulate the spread of COVID with masks and lockdown and vaccine.
simulate(population=8000000000, initial_cases=100, simulation_days=365, covid_r0=covid_r0, recovery_days=14, immune_days=200, save_file=True, policies=["MASKS", "LOCKDOWN", "VACCINE"], filename="data/masks_and_lockdown_and_vaccine.csv")