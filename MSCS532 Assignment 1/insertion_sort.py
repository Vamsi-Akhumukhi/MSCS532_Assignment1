def insertion_sort(array, order):
    """Sort an array in increasing or decreasing order."""
    order = order.strip().lower()

    if order not in ("increasing", "decreasing"):
        raise ValueError("Order must be 'increasing' or 'decreasing'.")

    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0:
            if order == "increasing":
                should_shift = array[i] > key
            else:
                should_shift = array[i] < key

            if not should_shift:
                break

            array[i + 1] = array[i]
            i -= 1

        array[i + 1] = key

    return array


if __name__ == "__main__":
    numbers = [31, 41, 59, 26, 41, 58]
    print("Numbers:", numbers)

    while True:
        sort_order = input("Choose increasing or decreasing order: ").strip().lower()
        if sort_order in ("increasing", "decreasing"):
            break
        print("Please enter 'increasing' or 'decreasing'.")

    insertion_sort(numbers, sort_order)
    print(f"Sorted in {sort_order} order:", numbers)