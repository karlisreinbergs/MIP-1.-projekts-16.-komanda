class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state 
        self.parent = parent  
        self.children = []  
        self.value = None  

    def add_child(self, child_state):
        child_node = TreeNode(child_state, parent=self)
        self.children.append(child_node)
        return child_node
