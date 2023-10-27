initial_cases = 7769783
final_cases = 12741386
days = 28 # Days between 8-6-2020 and 6-7-2020

# Calculate alpha.
alpha = 0.03

for i in range(1000):
    cases = initial_cases

    for i in range(days):
        cases = cases + int(cases * alpha)

    # Change alpha
    if final_cases - cases < 0:
        alpha = alpha - 0.0001
    if final_cases - cases > 0:
        alpha = alpha + 0.0001
    if final_cases - cases == 0:
        break

print(f"Alpha Value: {alpha}") # Alpha Value: 0.017800000000000073

# Calculate cases on December 31st 2020
cases = final_cases # Cases from 6-7-2020
days = 178 # Days between 6-7-2020 and 31-12-2020
alpha = 0.01782175760401952 # Alpha Value as previously calculated 

with open("simple_model.csv", "w") as f:
    for i in range(days):
        cases = cases + int(cases * alpha)
        print(f"Day {i+1}, {cases}", file=f)