# C сами массивами и базовыми навыками работы с ними я ознакомлен так что пример ниже будет примером

class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextbox = None


class LinkedList:
    def __init__(self):
        self.head = None


def contains(self, cat):
    lastbox = self.head
    while lastbox:
        if cat == lastbox.cat:
            return True
        else:
            lastbox = lastbox.nextbox
    return False

box = Box('маркиза', 1)

print(contains(box))

