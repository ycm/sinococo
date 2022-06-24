class Node:
    def __init__(self, glyph, type_):
        self.glyph = glyph
        self.type_ = type_
        self.parent = None
        self.children = []
    def __repr__(self):
        return f"<Node '{self.glyph}' with {len(self.children)} children>"

import pickle as pkl

def load_database():
    with open('data/database.pkl', 'rb') as f:
        return pkl.load(f)
