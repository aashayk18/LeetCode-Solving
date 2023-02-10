# Intuition
Check the string for the character whose frequency is 1.

# Approach
Use the `collections.Counter()` method to create a hash table of the elements of the string. Use the `items()` method to get the elements of the hash table along with their frequencies. Iteratively, use the variables `i` and `j` to find out the element with frequency 1 i.e. the corresponding `i` value for which the value of `j` is 1. Return the index of such an `i` in the string `s`. Finally, return -1 for the case in which there exists no unique character in the string.

# Complexity
- Time complexity:
$O(N)$

- Space complexity:
$O(N)$
