class Reader:
    def read(self, path):
        return open(path, "r", encoding='utf-8').read()
