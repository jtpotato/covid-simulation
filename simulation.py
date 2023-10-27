import random

def simulate(population, initial_cases, simulation_days, covid_r0, recovery_days, immune_days, policies=[], save_file = False, filename = "results.csv"):
    cases = [initial_cases]
    immune = []
    recovered = 0

    policies_active = False

    with open(filename, "w") as f:
        print(f"Day, Cases, New Cases, Recovered, Population", file=f)
        
        for day in range(simulation_days):
            # Apply policies
            if not policies_active and sum(cases) > population * 0.05:
                if "MASKS" in policies:
                    covid_r0 = covid_r0 * 0.25
                if "LOCKDOWN" in policies:
                    covid_r0 = covid_r0 * 0.1
                if "VACCINE" in policies:
                    covid_r0 = covid_r0 * 0.5
                policies_active = True

            # Find proportion of uninfected people
            infectable_proportion = 1 - ((sum(cases) + sum(immune)) / population)

            # Use random chance to simulate infections for small numbers.
            if sum(cases) < 50:
                new_cases_today = 0
                for i in range(sum(cases)):
                    # the channce of a person being infected is COVID's R0 number, spread out over the days a person is infectious
                    # (the R0 number is the number of people an infected person will infect, through the entire duration of the infection)
                    # currently infected people cannot be infected again, so we only infected the portion of the population that is not infected
                    if random.random() < (covid_r0 / recovery_days) * infectable_proportion:
                        new_cases_today += 1
                cases.append(new_cases_today)
            else:
                cases.append(int(sum(cases) * (covid_r0 / recovery_days) * infectable_proportion))

            # Remove cases that have recovered
            if len(cases) > recovery_days:
                recovered_today = cases.pop(0) # currently not used
                recovered += recovered_today
                immune.append(recovered_today)

            # Remove cases that have become immune
            if len(immune) > immune_days:
                immune.pop(0)

            print(f"Day {day+1}, added {cases[-1]} cases, total {sum(cases)} cases.")
            if save_file:
                print(f"{day}, {sum(cases)}, {cases[-1]}, {recovered}, {population}", file=f)

    return cases