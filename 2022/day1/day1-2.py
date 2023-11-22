
with open("input") as f:
	calories = f.read()

arr = calories.split("\n")

max_cals = 0
current = 0
cals = []
for i in arr:
	if not i:
		cals.append(current)
		current = 0
	else:
		current += int(i)

cals.sort(reverse=True)
print(sum(cals[:3]))
