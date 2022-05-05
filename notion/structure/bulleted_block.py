class BulletedBlock:

    def __init__(self, root, id, has_children, text, bold=False, italic=False, strikethrough=False, underline=False):
        self.root = root
        self.id = id
        self.has_children = has_children

        self.text = text
        self.bold = bold
        self.italic = italic
        self.strikethrough = strikethrough
        self.underline = underline

        self.children = []

    def insert(self, child_node):
        self.children.append(child_node)
