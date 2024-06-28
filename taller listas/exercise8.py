min_temperatures = []
max_temperatures = []

for i in range(5):
    min_temp = float(input(f"Enter the minimum temperature for day {i+1}: "))
    max_temp = float(input(f"Enter the maximum temperature for day {i+1}: "))
    min_temperatures.append(min_temp)
    max_temperatures.append(max_temp)

average_temperatures = []
for i in range(5):
    avg_temp = (min_temperatures[i] + max_temperatures[i]) / 2
    average_temperatures.append(avg_temp)

min_temperature = min(max_temperatures)

days_with_min_temp = []
for i in range(5):
    if max_temperatures[i] == min_temperature:
        days_with_min_temp.append(i)

temperature_to_find = float(input("Enter a temperature to find matching maximum temperatures: "))

matching_days = []
for i in range(5):
    if max_temperatures[i] == temperature_to_find:
        matching_days.append(i + 1)

print("\nAverage temperatures for each day:")
for i in range(5):
    print(f"Day {i+1}: {average_temperatures[i]:.2f}")

print("\nDays with the minimum temperature:", days_with_min_temp)

if matching_days:
    print(f"\nDays with maximum temperature matching {temperature_to_find}°C: {matching_days}")
else:
    print(f"\nThere are no days with maximum temperature {temperature_to_find}°C.")

   

