def last_indexof_max(numbers):
    index = 0
    for i, _ in enumerate(numbers):
        if numbers[i] >= numbers[index]:
            index = i
    return index
