# Intuition
Recursively find the minimum depth of left and right subtrees of the binary tree and find the minimum out of the two.

# Approach
Check the condition for whether the root is absent or not, and return 0 if it is. Recursively call the minDepth function on the left and right children of the root node and assign the values to lt and rt variables respectively. Check if the values of lt and rt are non-negativr, and if so, return the minimum out of the two. Add 1 to the value (for the common root node for the subtrees). Finally, return the sum of the lt and rt variables (minimum depths of the left and right subtrees), with 1 added to it (for the root node of the binary tree).

# Complexity
- Time complexity:


- Space complexity:
