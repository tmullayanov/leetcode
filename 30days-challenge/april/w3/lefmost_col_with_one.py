class BinaryMatrix(object):

    def __init__(self, arr=[]):
        self.arr = arr
        self._n = len(arr)
        self._m = len(arr[0]) if arr else 0

    def get(self, x: int, y: int):
        return self.arr[x][y]

    def dimensions(self):
        return [self._n, self._m]


def findLeftmostColWithOne(binaryMatrix):
    n, m = binaryMatrix.dimensions()
    res = -1

    x, y = 0, m - 1
    while x < n and y >= 0:
        if binaryMatrix.get(x, y) == 1:
            res = y
            y -= 1
        else:
            x += 1
    return res
