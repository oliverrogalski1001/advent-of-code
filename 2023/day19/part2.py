from ranges import Range
from copy import deepcopy

class Workflow:
    def __init__(self, type, operator, num, dest):
        self.type = type
        self.op = operator
        self.num = num
        self.dest = dest

class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def sum(self):
        return self.x + self.m + self.a + self.s

with open("input", "r") as f:
    works = {}
    parts = []
    section = False
    for line in f.readlines():
        if line == "\n":
            section = True
            continue
        if section:
            line = line.strip()[1:-1]
            ps = line.split(",")
            p = [int(ps[i][2:]) for i in range(len(ps))]
            parts.append(Part(p[0], p[1], p[2], p[3]))

        else:
            work_id, rest = line.split("{")
            work_steps = rest[:-1].split(",")
            steps = []
            for step in work_steps[:-1]:
                t = step[0]
                op = step[1]
                num = int(step[2:step.index(":")])
                dest = step[step.index(":") + 1:]
                wf = Workflow(t, op, num, dest)
                steps.append(wf)
            steps.append(work_steps[-1][:-1])
            works[work_id] = steps

start_ranges = {c: Range(1, 4000 + 1) for c in "xmas"}



print(start_ranges)
