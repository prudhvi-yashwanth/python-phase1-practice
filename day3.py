from typing import List, Dict

# Problem 1 — Count words in a sentence
def count_words(sentence: str) -> int:
    words = sentence.split()
    return(len(words))

if __name__ == '__main__':
   assert print(count_words('The biggest plant a man')) == 5
   assert print(count_words('     The biggest  the the the    plant a man.      ')) == 8


# Problem 2 — Multiply all numbers in a list
def product_of_list(numbers: list) -> int:
    if len(numbers) == 0:
        return('List cannot be Empty')
    result = 1
    for num in numbers:
        result *= num
    return result
print(product_of_list([]))

if __name__ == '__main__':
    assert print(product_of_list([2,4])) == 8 


# Problem 3 — Return only even numbers using list comprehension
def filter_even(nums: list) -> list:
    if len(nums) != 0 and isinstance(nums, list):
        return[number for number in nums if number%2 == 0]
    return('List cannot be empty or the input is not of type list')

if __name__ == '__main__':
    assert print(filter_even([12,2,3,4,5,5,7,9,23,4,6])) == [12, 2, 4, 4, 6]
    assert print(filter_even([])) == 'List cannot be empty or the input is not of type list'

# Problem 4 — Find the longest word in a sentence
def longest_word(sentence: str) -> str:
    words = sentence.split()
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

if __name__ == '__main__':
    assert print(longest_word('The mangoes are in betweennnnnnnnnn the baskets')) == 'betweennnnnnnnnn'
    assert print(longets)


#Problem 5 — Check if two strings are anagrams
def is_anagram(a: str, b: str) -> bool:
    a = a.lower()
    b = b.lower()
    if sorted(a) == sorted(b):
        return('The two words are anagram')
    else:
        return('The words are not anagram')

def is_anagram(a: str, b:str) -> bool:
    nomilization = lambda s: "".join(ch.lower() for ch in s if ch.isalnum())
    return sorted(nomilization(a)) == sorted(nomilization(b)) 

if __name__ == '__main__':
    assert print(is_anagram('listen', 'silent')) == 'The two words are anagram'
    assert print(is_anagram('earth', 'heArt')) == 'The two words are anagram'


# Problem 6 — Frequency count of characters
def char_frequency(s: str) -> dict:
    if len(s) != 0:
        return{char:s.count(char) for char in set(s)}
    return('The string cannot be empty')

print(char_frequency('mangomango'))


# Problem 7 — Remove vowels from a string
def remove_vowels(s: str) -> str:
    s = s.lower()
    new_word = []
    vowles = set('aeiouAEIOU')
    return(i for i in s if i not in s)

print(remove_vowels('mango'))
print(remove_vowels('aeiouAEIOU'))


# Problem 8 — Generate Fibonacci list of N terms
def fibonacci(n: int) -> list:
    empty_list = []
    a,b = 0,1
    for i in range(0, n):
        a,b = b, a+b 
        empty_list.append(a)
    return empty_list
print(fibonacci(10))

# Problem 9 — Convert list of Celsius values to Fahrenheit
def convert_to_fahrenheit(celsius_list: list) -> list:
    return[ c*1.8 + 32 for c in celsius_list]

convert_to_fahrenheit([12,3,4,55,56])

# Problem 10 — Implement manual min function
def find_min(nums: list) -> int:
    if len(nums) != 0 and isinstance(nums, list):
        min_number = nums[0]
        for i in nums:
            if i < min_number:
                min_number = i 
        return min_number
    else:
        return('Please enter a valid input')

print(find_min([12,2,3,4,5,12,3,4,5,5]))



# Correct Version of code
# day3_problems_clean.py
from typing import List, Dict

# Problem 1 — Count words in a sentence
def count_words(sentence: str) -> int:
    """Return number of words in sentence (split on whitespace)."""
    return len(sentence.split())

# Problem 2 — Multiply all numbers in a list
def product_of_list(numbers: List[int]) -> int:
    """Return product of numbers. Raise ValueError on empty list."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")
    result = 1
    for num in numbers:
        result *= num
    return result

# Problem 3 — Return only even numbers using list comprehension
def filter_even(nums: List[int]) -> List[int]:
    """Return list with only even numbers. Returns empty list for empty input."""
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    return [n for n in nums if isinstance(n, int) and n % 2 == 0]

# Problem 4 — Find the longest word in a sentence
def longest_word(sentence: str) -> str:
    """Return the longest word; if empty sentence, return empty string."""
    words = sentence.split()
    if not words:
        return ""
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

# Problem 5 — Check if two strings are anagrams
def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are anagrams (ignores spaces and case)."""
    normalize = lambda s: "".join(ch.lower() for ch in s if ch.isalnum())
    return sorted(normalize(a)) == sorted(normalize(b))

# Problem 6 — Frequency count of characters
def char_frequency(s: str) -> Dict[str, int]:
    """Return frequency dict of characters (O(n))."""
    freq: Dict[str,int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Problem 7 — Remove vowels from a string
def remove_vowels(s: str) -> str:
    """Return string with vowels removed (preserves case)."""
    vowels = set("aeiouAEIOU")
    return "".join(ch for ch in s if ch not in vowels)

# Problem 8 — Generate Fibonacci list of N terms
def fibonacci(n: int) -> List[int]:
    """Return first n Fibonacci numbers (0-indexed: [0,1,1,2...])."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    res = [0, 1]
    for _ in range(2, n):
        res.append(res[-1] + res[-2])
    return res

# Problem 9 — Convert list of Celsius values to Fahrenheit
def convert_to_fahrenheit(celsius_list: List[float]) -> List[float]:
    """Convert list of Celsius values to Fahrenheit."""
    return [c * 1.8 + 32 for c in celsius_list]

# Problem 10 — Implement manual min function
def find_min(nums: List[int]) -> int:
    """Return minimum of list. Raises ValueError for empty list."""
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")
    if not nums:
        raise ValueError("Please enter a non-empty list.")
    m = nums[0]
    for x in nums:
        if x < m:
            m = x
    return m

# -------------------------
# Quick tests (run as script)
if __name__ == "__main__":
    # Problem 1
    assert count_words('The biggest plant a man') == 5
    assert count_words('     The biggest  the the the    plant a man.      ') == 8

    # Problem 2
    try:
        product_of_list([])
        raise AssertionError("product_of_list should raise on empty")
    except ValueError:
        pass
    assert product_of_list([2, 4]) == 8

    # Problem 3
    assert filter_even([12,2,3,4,5,5,7,9,23,4,6]) == [12,2,4,4,6]
    assert filter_even([]) == []

    # Problem 4
    assert longest_word('The mangoes are in betweennnnnnnnnn the baskets') == 'betweennnnnnnnnn'
    assert longest_word('') == ""

    # Problem 5
    assert is_anagram('listen', 'silent') is True
    assert is_anagram('earth', 'heArt') is True
    assert is_anagram('hello', 'bello') is False

    # Problem 6
    assert char_frequency('mangomango')['m'] == 2

    # Problem 7
    assert remove_vowels('mango') == 'mng'
    assert remove_vowels('AeIoU') == ''

    # Problem 8
    assert fibonacci(1) == [0]
    assert fibonacci(6) == [0,1,1,2,3,5]
    assert fibonacci(0) == []

    # Problem 9
    assert convert_to_fahrenheit([0, 100]) == [32.0, 212.0]

    # Problem 10
    assert find_min([12,2,3,4,5,12,3,4,5,5]) == 2
    try:
        find_min([])
        raise AssertionError("find_min should raise on empty")
    except ValueError:
        pass

    print("All Day-3 tests passed ✅")