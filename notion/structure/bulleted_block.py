

class BulletedBlock:

    def __init__(self, root, id, has_children, text):
        self.root = root
        self.id = id
        self.has_children = has_children
        self.text = text
    
        self.children = []





    def insert(self, child_node):
        self.children.append(child_node)

    def get_data(self):
        return self.data
    
    def get_child(self):
        return self.children