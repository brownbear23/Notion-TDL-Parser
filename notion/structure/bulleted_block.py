class BulletedBlock:

    def __init__(self, root, id, has_children, texts):
        self.root = root
        self.id = id
        self.has_children = has_children

        self.texts = texts

        self.children = []

    def insert(self, child_node):
        self.children.append(child_node)
