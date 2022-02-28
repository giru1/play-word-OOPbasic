class Player:
    def __init__(self, name):
        self.name = name
        self.words = []
        self.scores = 0

    def __repr__(self):
        return self.name
