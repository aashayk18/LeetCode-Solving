# Intuition
Visit the root node, and then visit the children of the root node recursively.

# Approach
Check to see if the `root` exists. If it does, add it to an `ans` array. Iterate over the children of the root node, and append nodes to the ans array by recursively calling the `preorder()` function on each node. Finally, return the `ans` array.

# Complexity
- Time complexity:


- Space complexity:
