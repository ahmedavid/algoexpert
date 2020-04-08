class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, value):
        self.children.append(Node(value))
    
    #O(v+e) time | O(v) space
    def depthFirstSearch(self, array: List()):
        array.append(self.value)
        for child in self.children:
            child.depthFirstSearch(array)
        return array