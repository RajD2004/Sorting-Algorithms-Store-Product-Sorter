
from typing import TypeVar, List, Callable

T = TypeVar("T")  # represents generic type


# This is an optional helper function but HIGHLY recommended, especially for the application problem!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Compares two elements based on a custom comparator function and a specified sorting order.

    :param first: The first element to compare.
    :param second: The second element to compare.
    :param comparator: A callable function that compares two elements and returns a boolean indicating the comparison result.
    :param descending: A boolean flag that indicates whether the comparison should be performed in descending order. If True,
    the comparator will be applied with the arguments swapped to achieve descending order.
    :return: A boolean result from the comparator function, indicating the result of the comparison.
    """
    if descending:
        return comparator(second, first)
    else:
        return comparator(first, second)


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Performs an in-place selection sort on a list of elements, using a custom comparator function and optional descending order.

    :param data: A list of elements to be sorted.
    :param comparator: A callable function that compares two elements and returns a boolean indicating their order. By default,
    it compares in ascending order (i.e., x < y).
    :param descending: A boolean flag that indicates whether the sort should be in descending order. If True, the comparator will
    be adjusted to perform the sort in reverse order.
    :return: None. The sorting is done in place, modifying the original list.
    """
    for outer_index in range(len(data) - 1):
        smallestIndex = outer_index
        for inner_index in range(outer_index + 1, len(data)):
            if do_comparison(data[inner_index], data[smallestIndex], comparator, descending):
                smallestIndex = inner_index
        data[smallestIndex], data[outer_index] = data[outer_index], data[smallestIndex]


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Performs an in-place bubble sort on a list of elements, using a custom comparator function and optional descending order.

    :param data: A list of elements to be sorted.
    :param comparator: A callable function that compares two elements and returns a boolean indicating their order. By default,
    it compares in ascending order (i.e., x < y).
    :param descending: A boolean flag that indicates whether the sort should be in descending order. If True, the comparator will
    be adjusted to perform the sort in reverse order.
    :return: None. The sorting is done in place, modifying the original list.
    
    The algorithm iterates through the list, repeatedly swapping adjacent elements if they are in the wrong order based on the
    comparator. It continues this process until the list is sorted. If during an iteration no swaps are made, the algorithm
    terminates early.
    """
    for outer_index in range(len(data) - 1):
        is_sorted = True
        for inner_index in range(len(data) - outer_index - 1):
            if do_comparison(data[inner_index + 1], data[inner_index], comparator, descending):
                data[inner_index + 1], data[inner_index] = data[inner_index], data[inner_index + 1]
                is_sorted = False
        if is_sorted: return


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Performs an in-place insertion sort on a list of elements, using a custom comparator function and optional descending order.

    :param data: A list of elements to be sorted.
    :param comparator: A callable function that compares two elements and returns a boolean indicating their order. By default,
    it compares in ascending order (i.e., x < y).
    :param descending: A boolean flag that indicates whether the sort should be in descending order. If True, the comparator will
    be adjusted to perform the sort in reverse order.
    :return: None. The sorting is done in place, modifying the original list.

    The algorithm iterates through the list, starting from the second element. Each element is compared with the elements before
    it using the comparator, and it is inserted in its correct position relative to the already sorted part of the list. This
    process continues until the entire list is sorted.
    """
    for outer_index in range(1, len(data)):
        temp = data[outer_index]
        inner_index = outer_index - 1
        while inner_index >= 0 and do_comparison(temp, data[inner_index], comparator, descending):
            data[inner_index + 1] = data[inner_index]
            inner_index -= 1
        data[inner_index + 1] = temp


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Performs a hybrid merge sort on a list of elements. This algorithm switches to insertion sort for small subarrays
    to improve performance for nearly sorted or small datasets.

    :param data: A list of elements to be sorted.
    :param threshold: The size of subarrays at which the algorithm switches to insertion sort. If the length of the subarray is
    less than or equal to the threshold, insertion sort is used. The default is 12, which is generally efficient for small arrays.
    :param comparator: A callable function that compares two elements and returns a boolean indicating their order. By default,
    it compares in ascending order (i.e., x < y).
    :param descending: A boolean flag that indicates whether the sort should be in descending order. If True, the comparator will
    be adjusted to perform the sort in reverse order.
    :return: None. The sorting is done in place, modifying the original list.

    The hybrid merge sort works by recursively splitting the array into smaller subarrays. Once the size of a subarray reaches 
    the specified threshold, the algorithm switches to insertion sort for that subarray. After sorting the subarrays, they are 
    merged back together using the provided comparator function.
    """
    def merge(leftArray, rightArray, mainArray):
        left_index, right_index, main_index = 0, 0, 0

        while left_index < len(leftArray) and right_index < len(rightArray):
            if(do_comparison(leftArray[left_index], rightArray[right_index], comparator, descending)):
            #if(do_comparison(rightArray[right_index], leftArray[left_index], comparator, descending)):
                mainArray[main_index] = leftArray[left_index]
                main_index += 1
                left_index += 1
    
            else:
                mainArray[main_index] = rightArray[right_index]
                main_index += 1
                right_index += 1
        
        while left_index < len(leftArray):
            mainArray[main_index] = leftArray[left_index]
            main_index += 1
            left_index += 1
        
        while right_index < len(rightArray):
            mainArray[main_index] = rightArray[right_index]
            main_index += 1
            right_index += 1

    if (len(data) <= threshold and threshold > 0):
        insertion_sort(data, comparator=comparator, descending=descending)
        return
    elif len(data) < 2 and threshold <= 0:
        return 
    middle = len(data) // 2
    leftArray = data[:middle]
    rightArray = data[middle:]
    hybrid_merge_sort(leftArray, threshold=threshold, comparator=comparator, descending=descending)
    hybrid_merge_sort(rightArray, threshold=threshold, comparator=comparator, descending=descending)
    merge(leftArray, rightArray, data)

def quicksort(data: List[T]) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first: int, last: int) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)


###########################################################
# DO NOT MODIFY
###########################################################
class Product:
    """
    Class that represents products.
    """
    __slots__ = ['price', 'rating', 'relevance']

    def __init__(self, price: float, rating: int, relevance: float) -> None:
        """
        Constructor for the Product class.

        :param price: The price of the product.
        :param rating: The rating of the product.
        :param relevance: A score representing how closely the product matches the user's search keywords. A higher value
        indicates a stronger match between the product and the search query.
        :return: None
        """
        self.price = price
        self.rating = rating
        self.relevance = relevance

    def __repr__(self) -> str:
        """
        Represent the Product as a string.

        :return: Representation of the product.
        """
        return str(self)

    def __str__(self) -> str:
        """
        Convert the Product to a string.

        :return: String representation of the product.
        """
        return f'<price: {self.price}, rating: {self.rating}, relevance: {self.relevance}>'

    def __eq__(self, other) -> bool:
        """
        Compare two Product objects for equality based on price and rating.

        :param other: The other Product to compare with.
        :return: True if products are equal, False otherwise.
        """
        return self.price == other.price and self.rating == other.rating and self.relevance == other.relevance


###########################################################
# MODIFY BELOW
###########################################################


def recommend_products(products: List[Product], sorted_by: str) -> List[Product]:
    """
    Recommends a list of products based on their relevance and a secondary sorting criterion such as price or rating.

    :param products: A list of Product objects to be sorted and filtered.
    :param sorted_by: A string representing the secondary sorting criterion. It can be one of the following:
        - 'price_low_to_high': Sorts the products by price in ascending order. If two products have the same price, they
          are sorted by rating in descending order.
        - 'price_high_to_low': Sorts the products by price in descending order. If two products have the same price, they
          are sorted by rating in descending order.
        - 'rating': Sorts the products by rating in descending order. If two products have the same rating, they are sorted
          by price in ascending order.
    :return: A list of products representing the top 30% most relevant products, sorted by the specified criterion.

    The function first sorts the products by relevance in descending order, selects the top 30% most relevant products, and
    then sorts them according to the specified `sorted_by` criterion.
    """
    output_list = []
    hybrid_merge_sort(products, comparator= lambda p1, p2: p1.relevance < p2.relevance, descending=True)
    output_size = round(0.3 * len(products))
    output_list = products[:output_size]

    if sorted_by == "price_low_to_high":
        hybrid_merge_sort(output_list, comparator=lambda p1, p2: p1.price > p2.price if p1.price != p2.price else p1.rating < p2.rating, descending=True)

    elif sorted_by == "price_high_to_low":
        hybrid_merge_sort(output_list,comparator=lambda p1, p2: p1.price < p2.price if p1.price != p2.price else p1.rating < p2.rating, descending=True)
    
    elif sorted_by == "rating":
        hybrid_merge_sort(output_list, comparator= lambda p1, p2: p1.rating < p2.rating if p1.rating != p2.rating else p1.price > p2.price, descending=True)
    

    return output_list



print("HELLO WORLD")