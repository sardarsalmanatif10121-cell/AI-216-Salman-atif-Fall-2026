# Input: list of temperature readings
# Processing: classify each reading, count categories
# Output: category for each reading and final summary

temperatures = [21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]

below_normal = 0
normal = 0
high = 0

for temp in temperatures:
    if temp < 15:
        print(f"{temp}°C → Below Normal")
        below_normal += 1
    elif temp <= 30:
        print(f"{temp}°C → Normal")
        normal += 1
    else:
        print(f"{temp}°C → High")
        high += 1

print("\n--- Summary ---")
print(f"Below Normal: {below_normal}")
print(f"Normal: {normal}")
print(f"High: {high}")