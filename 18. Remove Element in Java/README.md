# Intuition
Traverse the array and check if the element exists in the array, and remove it.

# Approach
Initialize a count variable with 0. Run a for loop to traverse the length of the array, and check if the elements of the array match the given element. If they don't, move the element at the current index position to the index position given by count. Then, increment count. Finally, return the value of count. This value of count represents the number of elements at the start of the array which do not include val.

# Complexity
Time complexity:

Space complexity:
