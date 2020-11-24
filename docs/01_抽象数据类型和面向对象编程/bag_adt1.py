class Bag(object):
    """
    背包类型
    """
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = []

    def add(self, item):
        if len(self._items) < self.maxsize:
            self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        yield from self._items


def test_bag():
    bag = Bag(4)
    bag.add(1)
    bag.add(2)
    bag.add(3)
    assert(len(bag)==3)

    bag.remove(2)
    assert(len(bag)==2)

    value = [x for x in bag]
    assert(value == [1, 3])


if __name__ == "__main__":
    test_bag()
