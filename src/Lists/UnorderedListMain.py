from UnorderedList import UnorderedList

# Example Usage:
my_list = UnorderedList()
my_list.add(3)
my_list.add(7)
my_list.append(10)
print(my_list.size)  # Output: 3
print(my_list.search(7))  # Output: True
my_list.remove(7)
print(my_list.size)  # Output: 2
print(my_list.is_empty)  # Output: False
print(my_list.pop())  # Output: 10
print(my_list.size)  # Output: 1
