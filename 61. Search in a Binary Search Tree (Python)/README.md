# Intuition
Recursively search the left and right subtrees of the root node to find the required value.

# Approach
Check if the root exists and if the value of the root is greater than `val`, then recursively call the function on the left subtree of the root node. Similarly, if the root exists and the value of the root is lesser than `val`, then recursively call the function on the right subtree of the root node. In the end, return the root node.

# Complexity
- Time complexity:


- Space complexity:
