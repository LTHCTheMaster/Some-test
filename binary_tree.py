###############################################################################
# This programm is built to manage Research Binary Tree
###############################################################################

# Define Research Binary Tree class
class ResearchBinaryTree:

    # Constructor of ResearchBinaryTree class
    def __init__(self, value:float=None):
        self.left = None
        self.right = None
        self.value = value
    
    # Insert a value in the ResearchBinaryTree
    def insert(self, value:float):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = ResearchBinaryTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = ResearchBinaryTree(value)
            else:
                self.right.insert(value)
