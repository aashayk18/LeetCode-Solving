# Intuition
Performing XOR operation over the elements in the list will give the answer, as the XOR of two equal values gives 0.

# Approach
Use the reduce() function available in the functools library in Python, to run the XOR function across all the elements in the list. This returns the value of the element for which the answer is not 0, as it will be the only number without a duplicate and hence XOR'ing it will result in a non-zero value.

# Complexity
- Time complexity:


- Space complexity:
