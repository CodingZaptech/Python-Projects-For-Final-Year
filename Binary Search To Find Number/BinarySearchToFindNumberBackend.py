# BinarySearchToFindNumberBackend.py
# Backend logic for binary search implementation

class BinarySearch:
    def __init__(self, data: list):
        # Ensure the list is sorted before searching
        self.data = sorted(data)

    def search(self, target: int) -> int:
        """
        Performs binary search on the sorted list.
        :param target: number to search
        :return: index if found, -1 otherwise
        """
        low, high = 0, len(self.data) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
