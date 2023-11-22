
with open("input") as f:
    f = f.read()

for i in range(3, len(f)):
    slice = f[i - 3: i + 1]
    if len(set(slice)) == len(slice):
        print(i + 1)
        break
