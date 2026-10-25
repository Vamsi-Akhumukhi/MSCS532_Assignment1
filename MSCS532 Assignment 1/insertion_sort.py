def insertion_sort(array):
    """Sort an array in increasing order using insertion sort."""
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1

        array[i + 1] = key

    return array

if __name__ == "__main__":
    numbers = [31, 41, 59, 26, 41, 58]
    print("Before sorting:", numbers)
    insertion_sort_descending(numbers)
    print("After sorting: ", numbers)