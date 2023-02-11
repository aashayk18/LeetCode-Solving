# Intuition
Compare the lengths of the given array and a set version of the array.

# Approach
Get the length of the given array using the `len()` function. Use the `set()` function to convert the given array into a set i.e. every element is unique, thus disallowing repeated elements. Get the length of this set and compare it with the previously obtained array length to check that it isn't equal. If it isn't equal, it means that we have a repeated element. If it is equal, it means that no element is repeated. Return the boolean value of the expression.

# Complexity
- Time complexity:


- Space complexity:
