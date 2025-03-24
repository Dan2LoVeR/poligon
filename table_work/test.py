class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0
    def __iter__(self):
        return self
    def __next__(self):
        