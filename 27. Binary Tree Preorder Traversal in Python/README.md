# Intuition
Recursively traverse the nodes of the binary tree in a preorder manner.

# Approach
Create an empty results array. Create a traverse function which takes a node of the binary tree as input. Then the value of the node is added to the results array. If it has a left child, the function is recursively applied to it.  Then if the node has a right child, the function is recursively applied to it. Inside the solution class, we then call the traverse function on the given input root node if the input isn't blank. Finally, we return the results array.

# Complexity
- Time complexity:


- Space complexity:
