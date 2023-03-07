class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [(root, 0)]
        lvl_val = defaultdict(list)
        while stack:
            curr_node, curr_lvl = stack.pop()
            lvl_val[curr_lvl].append(curr_node.val)
            if curr_node.right:
                stack.append((curr_node.right, curr_lvl+1))
            if curr_node.left:
                stack.append((curr_node.left, curr_lvl+1))
        return [sum(val)/len(val) for val in lvl_val.values()]
