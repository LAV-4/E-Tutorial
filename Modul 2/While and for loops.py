dose = 5.0
degradation_rate = 0.1
times = 50

print("t | concentration in blood")
print("*************************")

for time in range(0, times):
    print(time, " ", dose)
    dose = dose * (1-degradation_rate)
