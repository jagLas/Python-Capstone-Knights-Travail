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

    def depth_search(self, value):
        if self.value == value:
            return self
        
        if len(self.children) > 0:
            left_result = self.children[0].depth_search(value)
            if left_result is not None:
                return left_result
        
        if len(self.children) > 1:
            if self.children[1].depth_search(value) is not None:
                return self.children[1].depth_search(value)

        return None
    
    def breadth_search(self, value):
        queue = [self]

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.value == value:
                return current_node 
            
            for child in current_node.children:
                queue.append(child)

        return None