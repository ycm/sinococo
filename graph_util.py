class Composition:
    def __init__(self, data):
        self.classification = "composition"
        self.symbol = data
        self.children = []
        self.parent = None

class Char:
    def __init__(self, data):
        self.classification = "char"
        self.symbol = data
        self.child = None
        self.parents = []