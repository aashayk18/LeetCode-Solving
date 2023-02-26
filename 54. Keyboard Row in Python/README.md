# Intuition
Check if the number of unique characters in a particular keyboard row is equal to the number of unique characters in the string of a particular word taken together with the keyboard row.

# Approach
Define the strings `l1`, `l2`, and `l3` that represent the characters of each of the three keyboard rows containing letters. Create an empty array `res`. Iterate over the `words` list, and convert the words to lowercase. For each word, check if the length of the set of unique characters in the word when taken together with each of the strings l1, l2, and l3 is equal to the respective strings. This reveals if the word can in fact be formed from using just the letters of one particular row, without adding any more additional characters. If this is the case, append the particular word to the `res` array. Finally, return the `res` array.

# Complexity
- Time complexity:


- Space complexity:
