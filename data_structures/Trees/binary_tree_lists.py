# Tree represented through lists
def BinaryTree(r):
	return [r,[],[]]

def insertLeft(root, newBranch):
	t = root.pop(1)

	# IF not empty
	if len(t) > 1:
		root.insert(1, [newBranch, t, []])
	else:
		root.insert(1, [newBranch,[],[]])

	return root

def insertRight(root, newBranch):
	t = root.pop(2)

	# If not empty
	if len(t) > 1:
		root.insert(1, [newBranch, [], t])
	else:
		root.insert(1, [newBranch,[],[]])
		
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root, newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root)
	return root[2]

r = BinaryTree(3)

insertLeft(r, 4)

insertLeft(r, 5)

insertRight(r, 6)

insertRight(r, 7)

