import random
def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swap = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swap = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

        if not swap: break  # break if collection sorted

    return collection

example_collection = [3, 1, 2 , -1, 0 , -2 , 5, 7]
example_collection = bubble_sort(example_collection)
print example_collection
# who change this line