class newnode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


# Driver Code
if __name__ == '__main__':
	root = newnode(10)
	root.left = newnode(5)
	root.right = newnode(15)
	root.left.left = newnode(2)
	root.left.right = newnode(5)
	root.left.left.left = newnode(1)
	root.right.right = newnode(22)
	root.right.left = newnode(13)
	root.right.left.right = newnode(14) 
	k = 12

# Avarage: O(log(n)) | O(log(n))
# Worst: O(n) time | O(n) space
# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree,target, float("inf"))

# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         return tree.value
#     if target < tree.value:
#         return findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         return findClosestValueInBstHelper(tree.right, target, closest) 
#     else:
#         return closest

# Avarage: O(log(n)) | O(log(n))
# Worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree,target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
           currentNode = currentNode.left
        elif target > currentNode.value:
           currentNode = currentNode.right 
        else:
            break
    return closest


print(findClosestValueInBst(root, k))


