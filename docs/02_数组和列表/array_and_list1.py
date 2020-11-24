class Array(object):
    """
    实现定长的 数组 ADT，省略了边界检查等
    """
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size
    
    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, item):
        self._items[index] = item

    def __len__(self):
        return self._size
    
    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value
    
    def __iter__(self):
        yield from self._items


def test_array():
    array = Array(4)
    array[0] = 1
    assert(array[0]==1)
    assert(array[1]==None)

    array.clear()
    assert([x for x in array] == [None] * 4)


if __name__ == "__main__":
    test_array()
