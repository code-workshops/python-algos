class BigO(object):
    """
    Big O Notation by example

    Each method below illustrates what algorithms of increasing complexity look like.
    """
    from copy import deepcopy

    def __init__(self, data_collection):
        """
        :params data_collection: represents the n variable of Big O
        """
        self.data = data_collection
        self._original = deepcopy(data_collection)

    def _restore(self):
        """Reset BigO with the original data set, unsorted."""
        self.data = self._original

    def add_item_to_list(self, value):
        """Constant O(1)

        The size of the array doesn't matter. It performs exactly the same.
        """
        self.data.append(value)


    def find_item(self, value):
        """Linear O(n)

        Time complete grows in direct proportion of the amount of the data.
        To find all items that match what we're searching for, we have to search each item of the array.
        """
        matches = []
        for item in self.data:
            if item == value:
                matches.append(item)
        return matches

    def bubble_sort(self):
        """O(n^2)

        Time to complete will be proportional to the square of the amount of data.

        Bubble sort gets slower as it processes. Poor performance.
        """
        for n in range(self.data-1, 0, -1):
            for i in range(n):
                if self.data[i] > self.data[i+1]:
                    tmp = self.data[i]
                    self.data[i] = self.data[i+1]
                    self.data[i+1] = tmp

    def binary_search(self, value):
        """O(logn)

        Data used decreases each time it's run. Extremely efficient.
        The inverse of exponential algorithms.
        """
        low = 0
        high = len(self.data) - 1
        while low <= high:
            middle = (high + low)/2
            if self.data[middle] < value:
                low = middle + 1
            elif self.data[middle] > value:
                high = middle + 1
            else:
                print("Match found.")
                low = high + 1

    def _partition(self, start, end, pivot):
        """For self.quick_sort."""
        self.data[pivot], self.data[end] = self.data[end], self.data[pivot]
        store_index = start
        for i in xrange(start, end):
            if self.data[i] < self.data[end]:
                self.data[i], self.data[store_index] = self.data[store_index], self.data[i]
                store_index += 1
        self.data[store_index], self.data[end] = self.data[end], self.data[store_index]
        return store_index

    def _sort(self, start, end):
        """For self.quick_sort"""
        if start >= end:
            return self.data
        pivot = randrange(start, end + 1)
        new_pivot = self._partition(start, end, pivot)
        self._sort(start, new_pivot - 1)
        self._sort(new_pivot + 1, end)

    def quick_sort(self):
        """O(nlogn)

        Values are only compared once, rather than repeatedly, with increasing efficiency.
        The amount of comparisons = log n + log(n-1) ...log(1) or n log n

        """
        self._sort(0, len(self.data) - 1)
        return self.data

    def merge_sort(self):

        return
