from typing import Any


t_addition = lambda t1, t2: (t1[0] + t2[0], t1[1] + t2[1])
find_all = lambda l, c: [i for i, x in enumerate(l) if x == c]


class CustomQueue:
    def __init__(self, arr=[]):
        self.arr = arr
        self.seen = arr.copy()

    def __repr__(self):
        return f"{self.arr}"

    def __eq__(self, val):
        return self.arr == val

    def append(self, add):
        if add not in self.seen:
            self.seen.append(add)
            self.arr.append(add)

    def pop(self, index=0):
        return self.arr.pop(index)

    def index(self, index):
        return self.arr[index]

    def length(self):
        return len(self.arr)


if __name__ == "__main__":
    q = CustomQueue()
    q.append(1)

    print(q)
    print(q.pop())
    q.append(1)
    q.append(2)
    print(q.length())
