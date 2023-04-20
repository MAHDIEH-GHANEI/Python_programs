def combine_trees(tree1, tree2):
    return tree1 + tree2

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
  
    if right < n and arr[right] > arr[largest]:
        largest = right
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapify_combined_tree(combined_tree):
    n = len(combined_tree)
    for i in range(n//2 - 1, -1, -1):
  
        heapify(combined_tree, n, i)
  
    return combined_tree

tree1 = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
tree2 = [7, 4, 15, 11, 13, 22, 16]

combined_tree = combine_trees(tree1, tree2)
heapified_tree = heapify_combined_tree(combined_tree)

print(heapified_tree)
