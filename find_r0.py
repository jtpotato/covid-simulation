import simulation


def find_r0(initial_cases, final_cases, days, iterations = 100):
    starting_r0 = 1
    covid_r0 = starting_r0

    for i in range(iterations):
        print(f"--------\nIteration {i}:")
        active_cases = sum(simulation.simulate(population=8000000000, initial_cases=initial_cases, simulation_days=days, covid_r0=covid_r0, recovery_days=14, immune_days=300, save_file=False))

        # Change covid_r0 slightly to get closer to final_cases
        if final_cases - active_cases < 0:
            covid_r0 = covid_r0 - 0.001
        if final_cases - active_cases > 0:
            covid_r0 = covid_r0 + 0.001
        if final_cases - active_cases == 0:
            break

    return covid_r0