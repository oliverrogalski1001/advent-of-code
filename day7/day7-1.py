
with open("input") as f:
    f = f.read().split("\n")


class Tree:
    def __init__(self, data, parent=None):
        self.children = []
        self.data = data
        self.parent = parent
        self.size = 0


wd = Tree("/")
for i in f:
    command = i.split(" ")
    if i[0] != "$":
        if i[0].isdigit():
            wd.children.append(int(i.split(" ")[0]))
        else:
            wd.children.append(Tree(i.split(" ")[1], wd))
        wd.size += 1
    elif command[1] == "cd":
        if command[2] != "..":
            for files in wd.children:
                if type(files) == Tree and files.data == command[2]:
                    wd = files
                    break
        else:
            wd = wd.parent

while wd.data != "/":
    wd = wd.parent

file_sizes = []


def size(tree: Tree):
    count = 0
    for j in tree.children:
        if type(j) != Tree:
            count += j
        else:
            x = size(j)
            file_sizes.append(x)
            count += x

    return count


file_sizes.append(size(wd))
print(sum(filter(lambda x: x <= 100000, file_sizes)))
