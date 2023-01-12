# Intuition
Check if there exist similar elements in the array by running a loop over it, and keep only the dissimilar elements.

# Approach
Check if the array length is 0, and in that case return 0. If not, initilaize i as 0 and run a loop from index 1 to the last index of the array. In this loop, check if the element at the index matches the element at index i, and if it doesn't increment i by 1 and set the element at this index. In the end, return the value of i+1 to indicate the number of unique elements.

# Complexity
Time complexity:

Space complexity:
