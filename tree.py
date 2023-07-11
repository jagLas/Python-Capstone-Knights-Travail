class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value
    
    @property
    def children(self):
        return self._children
    
    
    def add_child(self, child_node):
        if child_node not in self._children:
            self._children.append(child_node)
            child_node.parent = self
        else:
            return

    def remove_child(self, child_node):
        if child_node in self._children:
            self._children.remove(child_node)
            child_node.parent = None

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        if self.parent is parent:
            return
        
        if self.parent is not None:
            self.parent.remove_child(self)
        
        self._parent = parent

        if parent is not None:
            parent.add_child(self)

child1 = Node('child1')
parent = Node('parent')
child2 = Node('child2')

child1.parent = parent
child2.parent = parent