
weekend_temps = (24.5, 31.0, 28.2, 23.0, 29.5, 27.8)

print("Recorded Temperatures:")
for temp in weekend_temps:
    print(f"- {temp}°C")

highest_temp = max(weekend_temps)
lowest_temp = min(weekend_temps)

print(f"\nHighest Temperature: {highest_temp}°C")
print(f"Lowest Temperature:  {lowest_temp}°C")