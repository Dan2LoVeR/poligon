# Heaps, Stacks, Queues
from typing import Optional, List
from heapq import heappush, heappop, nlargest
from collections import deque


# Heaps ////////////////////////////////////////////////////////////////////////
class BinaryHeap:
    def __init__(self, elements: Optional[int] = None) -> None:
        if elements is not None:
            self.heap(elements)
        else:
            self.elements: List[int] = []
        self._lenght = None

    @property
    def lenght(self):
        self._lenght = len(self.elements)
        return self._lenght

    def add(self, element: int) -> None:
        self.elements.append(element)
        i = self.lenght - 1
        parent = int((i - 1) / 2)

        while i > 0 and list[i] > list[parent]:
            list[i], list[parent] = list[parent], list[i]
            i = parent
            parent = int((i - 1) / 2)

    def heapify(self, i: int):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.lenght:
            if self.elements[i] < self.elements[left]:
                self.elements[i], self.elements[left] = self.elements[left], self.elements[i]
                self.heapify(left)
        if right < self.lenght:
            if self.elements[i] < self.elements[right]:
                self.elements[i], self.elements[right] = self.elements[right], self.elements[i]
                self.heapify(right)

    def get_max(self) -> int:
        result = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop(-1)
        self.heapify(0)
        return result

    def heap(self, elements: List[int]):
        self.elements = elements
        for i in range(int(self.lenght / 2 + 1), -1, -1):
            self.heapify(i)


asteroid = deque(list(map(int, input().split())))

for item in asteroid:
    if item < 0:
        if item**2 < asteroid[(asteroid.index(item))-1]**2:
            asteroid.remove(item)
print(asteroid)


n, k = map(int, input().split())
numbers = list(map(int, input().split()))

heap = []

for idx, number in enumerate(numbers):
    number = str(number)
    for idx, digit in enumerate(numbers):
        value = int(digit) * (10 ** (len(number) - idx - 1))
        old_num = int(number)
        old_num -= value
        old_num += 9 * (10 ** (len(number) - idx - 1))
        heappush(heap, old_num - int(number))

print(sum(nlargest(k, heap)))
heap = BinaryHeap([10, 1, 99, 250, 50, 1000, 10000, 12])
print(heap.get_max())
print(heap.get_max())
print(heap.lenght)

# Stack ////////////////////////////////////////////////////////////////////////
