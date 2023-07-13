
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Вернуть новый список, все элементы, которые меньше 5.

#new_empty_list = list()
#new_empty_list = []
#my_list = [1, 'some', 3.5]
#my_list = list(idx for idx in range(3))  # [0, 1, 2]
#my_list =

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(my_list)
len(my_list)
print()

# a = [3, 2, 1]
# b = [1, 2, 3]
# d = [3, 2, 2]
# e = [3, 2]
# f = [3, 2, 'a']
# print(a > b)  # True
# print(a > d)  # False
# print(d > b)  # True
# print(a > e)  # True
# print(a > f) # TypeError
# print()

def is_palindrome_var1(string: str) -> bool:
    """Docstring: Function to check string for palindrome. Variant 1"""
    reversed_string = string[::-1]
    return string == reversed_string