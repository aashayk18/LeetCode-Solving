# Intuition
Check the number of unique characters in each string and when the strings are mapped to each other to see if there's an equal number of characters all around.

# Approach
Use the `set()` function to form sets of the individual unique characters of both strings `s` and `t`. Use the `zip()` function to map characters of `s` to the characters of `t`, and use the `set()` function on this to get a unique mappings so that each unique character in `s` is mapped to a unique character in `t`. Calculate the lengths of all these three sets and check if they are equal. If they are, we know that that there are exactly the same number of unique characters in both the strings to create a unique mapping to satisfy our condition of the strings being isomorphic i.e. one string can be formed by replacing the letters of the other. Return the boolean value for this expression.

# Complexity
- Time complexity:


- Space complexity:
