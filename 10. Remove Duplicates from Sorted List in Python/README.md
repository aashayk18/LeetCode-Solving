# Intuition
Traverse the list to check for duplicate elements and remove them.

# Approach
Check if the head pointer has no value, and if so, return it as is. Assign a new variable tmp to the value of the head pointer. Run a loop while there is a value after the tmp pointer. Check if the current value pointed to by the tmp pointer mathes the value pointed by the next of the tmp pointer, and if so make the next of tmp pointer move one step forward. If the pointers don't match, move the pointer forward one step. Return the head pointer.

# Complexity
Time complexity:

Space complexity:
