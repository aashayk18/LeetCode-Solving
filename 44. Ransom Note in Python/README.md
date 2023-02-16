# Intuition
Check if the number of occurrences of letters in one string match those of the other.

# Approach
Use the `collections.Counter()` method on `ransomNote` and `magazine` strings to form dictionaries with each unique character as a key and the number of its occurrences as the corresponding value. If the subtraction of these dictionaries gives an empty dictionary, we know that the string `ransomNote` can be formed from `magazine` as the characters are same in both. Return the boolean value of this expression.

# Complexity
- Time complexity:


- Space complexity:
