fname = input()

f = open(fname)
lines = f.readlines()
f.close()

class Tree:
	def __init__(self, name):
		self.name = name
		self.size = 0
		self.children = dict()
		self.parent = None
	def __eq__(self, other):
		return self.name == other.name
	def __repr__(self):
		string = f"name: {self.name}\nsize: {self.size}\nparent:{self.parent.name}\nchildren:"
		for child in self.children:
			string += f" {child},"
		for child in self.children:
			string += "\n\n" + str(self.children[child])
		return string

root  = Tree("root")
root.parent = root
currentTree = root
folders = set()
for line in lines:
	words = line.split()
	if words[0] == "$" and words[1] == "cd":
		branch = words[2]
		if branch == "/":
			currentTree = root
		elif branch == "..":
			currentTree = currentTree.parent
		else:
			name = currentTree.name + "/" +  branch
			currentTree = currentTree.children[name]
	
	elif words[0] == "$" and words[1] == "ls":
		continue
	else:
		name = currentTree.name + "/" + words[1]
		if name in currentTree.children:
			continue
		else:
			currentTree.children[name] = Tree(name)
			currentTree.children[name].parent = currentTree
		
		if words[0] != "dir":
			currentTree.children[name].size = int(words[0])


def setSizes(node):
	stack = [node]
	visited = set()
	while stack != []:
		top = stack.pop()
		if top.name in visited: 
			for child in top.children:
				top.size += top.children[child].size
		else:
			stack.append(top)
			for child in top.children:
				stack.append( top.children[child] )
			visited.add( top.name )

setSizes(root)
threshold = root.size - 40000000 
tightest = root.size
stack = [root]
while stack != []:
	top = stack.pop()
	if top.children == {}:
		continue
	for child in top.children:
		node = top.children[child]
		stack.append(node)
	if threshold <= top.size < tightest:
		tightest = top.size
	
print(tightest)

