class TksRegistry:
    def __init__(self):
        self.tks = []

    def add(self, tk):
        if len(self.tks) == 0:
            self.tks.append(tk)
            return True
        return False

    def clear(self):
        self.tks.clear()
        if len(self.tks) == 0:
            return True
        return False
