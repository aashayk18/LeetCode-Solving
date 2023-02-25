# Intuition
Visit the children of the root node recursively, and then visit the root node.

# Approach
Check to see if the `root` exists. If it does, create an empty `ans` array. Iterate over the children of the root node, and append nodes to the ans array by recursively calling the `postorder()` function on each node. Finally, return the `ans` array by appending the `root` node of the tree to it.

# Complexity
- Time complexity:


- Space complexity:
