1. Most list methods (like .append(), .extend(), .remove(), .sort()) modify the list in place.
Exception: Some operations like slicing (nums[1:3]) or + concatenation return a new list.

2. Strings in Python are immutable (cannot be changed in place).
Any method like .upper(), .replace(), .strip() returns a new string.


3. A set is an unordered collection → it doesn’t keep insertion order (before Python 3.7, even dicts didn’t).
Converting list → set → list will remove duplicates but may scramble order.

4. This is a special Python idiom. When you run a file directly, Python sets __name__ = "__main__".
When you import that file as a module, __name__ is set to the module’s name instead.

if __name__ == "__main__": ensures that the code inside this block only runs when the file is executed directly. If the file is imported as a module in another script, the code inside this block will not run.

5.assert is a debugging tool that checks whether a condition is true. If the condition is false, it raises an AssertionError, which helps identify problems during testing. If the condition is true, the program continues normally.