import simulation


def find_r0(initial_cases, final_cases, population, days, iterations = 100, mode="cumulative"):
    starting_r0 = 1
    covid_r0 = starting_r0

    for i in range(iterations):
        active_cases, cumulative_cases = simulation.simulate(population=population, initial_cases=initial_cases, simulation_days=days, covid_r0=covid_r0, immune_days=200, save_file=False)

        target_cases = 0

        if mode == "cumulative":
            target_cases = cumulative_cases
        elif mode == "active":
            target_cases = active_cases
        # Change covid_r0 slightly to get closer to final_cases
        if final_cases - target_cases < 0:
            covid_r0 = covid_r0 - 0.001
        if final_cases - target_cases > 0:
            covid_r0 = covid_r0 + 0.001
        if final_cases - target_cases == 0:
            break
    
    return covid_r0