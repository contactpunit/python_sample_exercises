class Stack:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def push(self, element):
        self._data.append(element)

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            return None
