
with open("input") as f:
	calories = f.read()

arr = calories.split("\n")

max_cals = 0
current = 0
for i in arr:
	if not i:
		if current > max_cals:
			max_cals = current
		current = 0
	else:
		current += int(i)

print(max_cals)