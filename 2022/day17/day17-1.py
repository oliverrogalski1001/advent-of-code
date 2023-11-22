
with open("input_test") as f:
    f = f.read()

shapes = [[(2, 3), (3, 3), (4, 3), (5, 3)],
          [(2, 4), (3, 3), (3, 4), (3, 5), (4, 4)],
          [(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)],
          [(2, 3), (2, 4), (2, 5), (2, 6)],
          [(2, 3), (2, 4), (3, 3), (3, 4)]]

floor = [0 for _ in range(7)]

for rock in range(2022):
    shape = shapes[rock % 5]
    for i in range(len(f)):
        direction = 1 if f[i] == ">" else -1
        temp = shape
        for j in range(len(shape)):
            if shape[j][0] not in range(7) or shape[] or shape[j][1] == floor[j]:
                shape = temp
                break
            shape[j] = (shape[j][0] + direction, shape[j][1])
            shape[j] = (shape[j][0] + direction, shape[j][1])



