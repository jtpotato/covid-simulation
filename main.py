import simulation_state

simulation = simulation_state.Simulation()

simulation.city_infected[0] = 1000 # initialise a patient zero at some point.

# Get the top 3 cities by population.
top_cities = sorted(simulation.city_populations, reverse=True)[:3]
# Get the index of the top 3 cities.
top_cities_index = [simulation.city_populations.index(city) for city in top_cities]
# Get the proportion of the population that lives in the top 3 cities.
top_cities_proportion = [city / sum(top_cities) for city in top_cities]

for day in range(28):
    simulation.print_state()

    # Loop over every city.
    for city in range(len(simulation.city_populations)):
        # Calculate how many people are going to travel.
        # The smaller the city, the larger % of the population will travel.
        if simulation.city_populations[city] < 500000:
            # 30% of the population will commute to larger cities.
            people_traveling = int(simulation.city_populations[city] * 0.3)
            # Of those, decide how many are infected.
            people_infected_travelling = int((simulation.city_infected[city] / simulation.city_populations[city]) * people_traveling)
            # print(people_infected_travelling)

            # Split the infected people between the top 3 cities based on the size of each.
            for j in range(len(top_cities)):
                simulation.city_commute_intake[top_cities_index[j]] += int(people_infected_travelling * top_cities_proportion[j])

        # Add new infections from within the city.
        potential_new_infections = int(simulation.city_infected[city] * 0.1)
        simulation.city_infected[city] += int(potential_new_infections * (1 - (simulation.city_infected[city] / simulation.city_populations[city])))

        # Add new infections from commuters.
        potential_new_infections = int(simulation.city_commute_intake[city] * 0.1)
        simulation.city_infected[city] += int(potential_new_infections * (1 - (simulation.city_infected[city] / simulation.city_populations[city])))