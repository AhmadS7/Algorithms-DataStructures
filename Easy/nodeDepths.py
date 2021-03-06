# O(n) time | O(h) space
def nodeDepths(root):
  sumOfObjects = 0
  stack = [{"node": root, "depth": 0}]
  while len(stack) > 0:
    nodeInfo = stack.pop()
    node, depth = nodeInfo["node"], nodeInfo["depth"]
    if node is None:
      continue
    sumOfDepths += depth
    stack.append({"node": node.left, "depth": depth + 1})
    stack.append({"node": node.right, "depth": depth + 1}) 
    
 return somOfDepths










class BinaryTree:
def __init__(self, value):
self.value = value
self.left = None
self.right = None