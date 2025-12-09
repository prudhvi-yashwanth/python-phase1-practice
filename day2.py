# Problem 1 — Sum of list
list_of_numbers = [1,2,34,56,12.0,4.44]
sum_of_numbers = 0
for number in list_of_numbers:
    sum_of_numbers += number
print(sum_of_numbers)
print(f'Sum of list of numbers are {sum(list_of_numbers)}')
print(f'Sum of numbers are {sum(list_of_numbers, start=10)}')


# Problem 2 — Count vowels in a string
word = input('Enter the string to calculate the words: ')
list_of_vowles = ['a', 'e', 'i', 'o', 'u']
count = 0
for letter in word.lower():
    if letter in list_of_vowles:
        count += 1
print(f'Total Number of vowles are: {count}')


# Problem 3 — Reverse a list (without using reverse() or slicing)
list_of_elements = ['fedx', 'Airone', 'S400', 'Tomcat', 12, 23, 00, 00.56, 00.00, 99.99]
revered_list = []
length_of_list = len(list_of_elements)

for i in range(1, length_of_list):
    revered_list.append(-i)
print(revered_list)

# Problem 3 — Reverse a list (without using reverse() or slicing)
list_of_elements = ['fedx', 'Airone', 'S400', 'Tomcat', 12, 23, 0, 0.56, 0.00, 99.99]
reversed_list = []
for i in range(len(list_of_elements) - 1, -1, -1):
    reversed_list.append(list_of_elements[i])
print("Problem 3 - reversed_list:", reversed_list)




# Problem 4 — Check palindrome (string)
palindrome_string = input('Enter the string to check palindrome')

nomralized_string = "".join(palindrome_string.lower().split())
print(nomralized_string)
if nomralized_string == nomralized_string[::-1]:
    print(f'The given word is a palandrom {nomralized_string}')


# Problem 5 — Find max and min in a list (without using built-in max()/min())
find_max_min = [12, 1, 4, 14, 33, 24.34, 99.45, 0, -7]
max_num = find_max_min[0]
min_num = find_max_min[0]
for i in find_max_min:
    if i > max_num:
        max_num = i 
    if i < min_num:
        min_num = i
print(max_num, min_num)


# Problem 6 — Remove duplicates while preserving order
list_of_numbers = [1, 2, 2, 3, 1]
seen = set()
result = []
for x in list_of_numbers:
    if x not in seen:
        seen.add(x)
        result.append(x)
print("Problem 6 - remove duplicates preserve order:", result)



# Problem 7 — Merge two lists and return sorted unique list
list1 = [1,3,3,5,6]
list2 = [1,2,3,4,5]
list1.extend(list2)
merged_sorted_list = sorted(set(list1))
print(merged_sorted_list)

# Problem 8 — Rotate list right by k
def rotate_list(lst, k=0):
    if isinstance(lst, list) and len(lst) != 0:
        k = k % len(lst)
        return lst[-k:] + lst[:-k]
    else:
        return "The list is empty"

rotate_list([1,2,3,4], 3)
rotate_list([12,3,4,5], 0)

# Problem 9 Fibonacci (nth number, iterative)
def fibonacci_iterative(number):
    a,b = 0,1
    for _ in range(number):
        a,b = b, a+b
    return a
print(fibonacci_iterative(6))


# Problem 10 — Two numbers in list add up to target (two-sum simple)
def two_sum_simple(lst, target):
    seen = {}
    for i, num in enumerate(lst):
        complement = target - num 
        if complement in seen:
            return(seen[complement], i)
        else:
            seen[num] = i
    return None
print(two_sum_simple([1,2,3,4,5], 9))


# Refactor block 


# Problem 8 — Rotate list right by k
def rotate_list(lst: list, k: int) -> list:
    """
    Rotate the list to the right by k positions.

    Input:
        lst (list): The list of elements
        k (int): Number of positions to rotate

    Returns:
        list: Rotated list
    """
    if not isinstance(lst, list) or len(lst) == 0:
        return "The list is empty"

    # Normalize k to avoid unnecessary full rotations
    k = k % len(lst)

    # Perform rotation
    return lst[-k:] + lst[:-k]


# ----------- TEST CASES -------------- #
if __name__ == "__main__":
    # Test rotation by 3
    assert rotate_list([1, 2, 3, 4], 3) == [2, 3, 4, 1]

    # Test rotation by 0 (should return same list)
    assert rotate_list([12, 3, 4, 5], 0) == [12, 3, 4, 5]

    # Rotation bigger than length
    assert rotate_list([10, 20, 30], 5) == [20, 30, 10]

    # Edge case
    assert rotate_list([1], 10) == [1]

    print("ALL TESTS PASSED!")


