⭐ FIRST — WHAT IS A TEST CASE?

A test case is simply:

A check to see if your function returns the correct output.

In Python, the simplest way to write a test is:

assert function_call == expected_output


If the assertion is true → program continues.
If false → program stops with an AssertionError.

⭐ HOW TO WRITE TESTS

There are two types of tests:

✔ 1. Normal tests

Check if output matches expected result.

Example:

assert count_words("hello world") == 2

✔ 2. Exception tests

Check if the function raises a specific error.

Example:

try:
    product_of_list([])  # should fail
    raise AssertionError("Expected ValueError but did not get it")
except ValueError:
    pass  # Good — test passed


Now let’s explain your three doubts.

🔥 PROBLEM-2 — product_of_list(numbers)

We expect:

If list is empty → function should raise ValueError

If list has numbers → return product

Your test code:

try:
    product_of_list([])
    raise AssertionError("product_of_list should raise on empty")
except ValueError:
    pass

🔍 WHY THIS WORKS?

You intentionally pass an empty list → expected to fail

Python runs product_of_list([])

Your function raises ValueError

Control jumps to except ValueError:

Test passes.

If your function did NOT raise an error,
Python would run the next line:

raise AssertionError("product_of_list should raise on empty")


This means:
❌ Fail the test because expected error did NOT happen.

Then the normal test:

assert product_of_list([2, 4]) == 8


Checks output is correct.

🔥 PROBLEM-6 — char_frequency(s)

Your function returns a dictionary like:

"mangomango" → {'m':2, 'a':2, 'n':2, 'g':2, 'o':2}


The test:

assert char_frequency('mangomango')['m'] == 2

🔍 WHY THIS WORKS?

Break it down:

char_frequency('mangomango') returns a dictionary.

['m'] accesses frequency of 'm'.

It must equal 2.

Example:

freq = char_frequency("mangomango")
freq['m']  # should be 2


This is how we test dictionaries.

🔥 PROBLEM-10 — find_min(nums)

Expected:

If empty → raise ValueError

If not → return minimum value

Your test:

assert find_min([12,2,3,4,5,12,3,4,5,5]) == 2


This is a normal test — checks output.

Next test:

try:
    find_min([])  # should raise
    raise AssertionError("find_min should raise on empty")
except ValueError:
    pass


Same exception logic as Problem-2.

If function behaves correctly:

Raises ValueError

Lands in except ValueError

Test passes

If not:

Goes to next line and raises
AssertionError("find_min should raise on empty")

⭐ NOW — LET ME SHOW YOU VISUALLY

So you never forget.

✔ 1. Normal assert test
assert f(2, 3) == 5


Means:
“If f(2,3) is not 5 → FAIL.”

✔ 2. Testing for errors template

Use this every time you expect a function to raise error.

try:
    function_call_that_should_fail()
    raise AssertionError("Function did NOT raise the expected error")
except ExpectedErrorType:
    pass  # test passed

This is EXACTLY how professional Python tests are written
(before using pytest).


⭐ SUMMARY TABLE (VERY EASY)
| Problem         | What are we testing?             | How test works                |
| --------------- | -------------------------------- | ----------------------------- |
| Product of list | Normal result + Empty list error | assert + try/except           |
| Char frequency  | Dictionary access                | `assert dict['key'] == value` |
| find_min        | Normal result + empty list error | assert + try/except           |
