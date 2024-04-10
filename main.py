# Find common values in multiple lists in Python

list1 = ['a', 'b', 'c']
list2 = ['a', 'z', 'c']
list3 = ['a', 'x', 'c']

common_elements = list(
    set(list1).intersection(list2, list3)
)
print(common_elements)  # 👉️ ['a', 'c']