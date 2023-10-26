import random
import city

cities = [city.City(population=random.randint(100000, 10000000), cases=0) for _ in range(10)]

cities[0].add_cases(1)

for i in range(365):
    for c in cities:
        c.simulate_day()

with open("results.csv", "w") as f:
    print(f"Day, {', '.join([f"City {c}" for c in range(len(cities))])}", file=f)
    for i in range(365):
        print(f"{i}, {", ".join([str(c.case_history[i]) for c in cities])}", file=f)
        print(f"{i}, {", ".join([str(c.case_history[i]) for c in cities])}") # print to console as well