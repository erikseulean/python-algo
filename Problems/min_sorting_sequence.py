

def start_sort(array):
    index = 1

    while index < len(array) and array[index] > array[index-1]:
        index += 1
    start = index - 1
    min_nr = 9999999
    for j in range(index, len(array)):
        min_nr = min(min_nr, array[j])
    while start > 0 and array[start-1] > min_nr:
        start -= 1

    return start

def end_sort(array):
    index = len(array) - 2
    while index >= 0 and array[index] < array[index+1]:
        index -= 1
    end = index + 1
    max_nr = -9999999
    for j in range(index, 0, -1):
        max_nr = max(max_nr, array[j])
    while end < len(array) - 1 and array[end+1] < max_nr:
        end += 1

    return end

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(start_sort(array), end_sort(array))