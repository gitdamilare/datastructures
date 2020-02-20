from ds2.sortedlistsimple import SortedListSimple

class SortedList(SortedListSimple):
    def __contains__(self, item):
        left, right = 0, len(self._L)
        while right - left > 1:
            median = (right + left) // 2
            if item < self._L[median]:
                right = median
            else:
                left = median
        return right > left and self._L[left] == item

