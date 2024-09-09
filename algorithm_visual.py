import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 1. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

# 2. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

# 3. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

# 4. Merge Sort
def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    mid = (left + right) // 2
    yield from merge_sort(arr, left, mid)
    yield from merge_sort(arr, mid + 1, right)
    yield from merge(arr, left, mid, right)
    yield arr

def merge(arr, left, mid, right):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    i, j, k = 0, 0, left

    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
        yield arr

    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
        yield arr

    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1
        yield arr

# 5. Corrected Quick Sort
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        yield from quick_sort(arr, low, pivot_index - 1)  # Sort left half
        yield from quick_sort(arr, pivot_index + 1, high)  # Sort right half
        yield arr  # Yield after partition to reflect the current state

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        yield arr  # Yield after each swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr  # Yield after the pivot is placed correctly
    return i + 1


def visualize_sorting(arr, sort_func):
    fig, ax = plt.subplots()
    ax.set_title(f"Visualizing {sort_func.__name__}")

    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]

    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"Iteration: {iteration[0]}")

    anim = animation.FuncAnimation(
        fig,
        func=update_fig,
        fargs=(bar_rects, iteration),
        frames=sort_func(arr.copy()),
        interval=100,
        repeat=False,
    )

    plt.show()


arr = np.random.randint(1, 100, size=20)


print("Visualizing Bubble Sort")
visualize_sorting(arr.copy(), bubble_sort)

print("Visualizing Selection Sort")
visualize_sorting(arr.copy(), selection_sort)

print("Visualizing Insertion Sort")
visualize_sorting(arr.copy(), insertion_sort)

print("Visualizing Merge Sort")
visualize_sorting(arr.copy(), merge_sort)

print("Visualizing Quick Sort")
visualize_sorting(arr.copy(), quick_sort)
