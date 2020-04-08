class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSumRecursive(tree: BinaryTree):
    sums = []
    branchSumRecursiveHelper(tree, 0, sums)
    return sums



def branchSumRecursiveHelper(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
 
    branchSumRecursiveHelper(node.left, newRunningSum, sums)
    branchSumRecursiveHelper(node.right, newRunningSum, sums)