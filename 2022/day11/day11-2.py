
with open("input") as f:
    f = f.read().split("\n\n")


class Monkey:
    def __init__(self, items, operation, test, success, fail):
        self.items = items
        self.operation = operation
        self.test = test
        self.success = success
        self.fail = fail
        self.ops = 0

    def inspect(self):
        op = self.operation[1]
        self.ops += 1
        if self.operation[1] == "old":
            op = self.items[0]

        if self.operation[0] == 0:
            self.items[0] *= op
        else:
            self.items[0] += op

        self.items[0] %= mod
        item = self.items.pop(0)
        if item % self.test == 0:
            return self.success, item
        else:
            return self.fail, item


monks = []
mod = 1
for monkey_string in f:
    stats = monkey_string.split("\n")
    items = list(map(lambda x: int(x), stats[1][stats[1].index(":") + 1:].strip().split(",")))
    operation = 0 if stats[2][stats[2].index("d") + 2] == "*" else 1
    try:
        operation_num = int(stats[2][stats[2].index("d") + 4:])
    except ValueError:
        operation_num = "old"
    operation_tuple = operation, operation_num
    test = int(stats[3][stats[3].index("y") + 2:])
    mod *= test
    success = int(stats[4][-1])
    fail = int(stats[5][-1])
    monks.append(Monkey(items, operation_tuple, test, success, fail))

for r in range(10000):
    for m in monks:
        for i in range(len(m.items)):
            to, level = m.inspect()
            monks[to].items.append(level)

sorted_list = sorted(list(map(lambda x: x.ops, monks)))[-2:]
monkey_business = 1
for level in sorted_list:
    monkey_business *= level
print(monkey_business)
