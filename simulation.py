import random

def simulate(population, initial_cases, simulation_days, covid_r0, immune_days, policies=[], save_file = False, filename = "results.csv"):
    cases = initial_cases
    immune = []
    to_recover = [int(initial_cases / 14)] * 14 + ([0] * simulation_days * 2) # spread recovery dates of initial cases over 14 days
    # pad list with (unnecessarily) additional 0s to avoid index errors
    cumulative_cases = initial_cases

    spread_rate = covid_r0

    with open(filename, "w") as f:
        print(f"Day, Total Cases, Active Cases, New Cases, Population", file=f)
        
        for day in range(simulation_days):
            # Remove cases that have recovered
            recovered_today = to_recover.pop(0)
            immune.append(recovered_today)
            cases -= recovered_today

            new_cases_today = 0

            # Find proportion of uninfected people
            infectable_proportion = 1 - ((cases + sum(immune)) / population)

            # Use random chance to simulate infections for small numbers.
            if cases < 50:
                for i in range(cases):
                    # the channce of a person being infected is COVID's R0 number, spread out over the days a person is infectious
                    # (the R0 number is the number of people an infected person will infect, through the entire duration of the infection)
                    # For simplicity, we assume that the R0 number is the same for every day of the infection
                    # and that the average infection time is 14 days.
                    # currently infected people cannot be infected again, so we only infected the portion of the population that is not infected
                    if random.random() < (spread_rate / 14) * infectable_proportion:
                        new_cases_today += 1
            else:
                new_cases_today = (int(cases * (spread_rate / 14) * infectable_proportion))
            
            cumulative_cases += new_cases_today
            cases += new_cases_today

            # Calculate new recovery dates for these cases
            for i in range(14):
                to_recover[i + 6] += int(new_cases_today / 14) # minimum 7 day infections, spread recovery dates over 14 days.
                # print(day)

            # Remove immunity numbers that are no longer immune (simple model)
            if len(immune) > immune_days:
                immune.pop(0)

            # print(f"Day {day+1}, added {cases[-1]} cases, total {sum(cases)} cases.")
            if save_file:
                print(f"{day}, {cumulative_cases}, {cases}, {new_cases_today}, {population}", file=f)

    return cases, cumulative_cases