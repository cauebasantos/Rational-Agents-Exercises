class Node:
    def __init__(self, content, children=[], parent=None):
        self.content = content
        self.children = children
        self.parent = parent

    def add_parent(self, parent):
        self.parent = parent

    def add_children(self, child):
        self.children.append(child)
