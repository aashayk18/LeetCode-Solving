# Intuition
Recursively calculate the depth of the left and right subtrees and determine the larger value.

# Approach
Return 0 as the depth if the root node is absent. Recursively call the function on the left and right subtrees, and add 1 to the value (for the level of each root node in the function call). Calculate the larger value out of the two and similarly add 1 to the result (for the root node of the tree). Return this value as the depth of the given binary tree.

# Complexity
- Time complexity:


- Space complexity:
