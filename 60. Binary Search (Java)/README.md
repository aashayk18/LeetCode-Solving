# Intuition
Split the array into half repeatedly until the middle element matches the target.

# Approach
Initalize `low` and `high` variables which mark the first and last elements of the array respectively. Start a while loop with the condition that `low` is less than or equal to `high`. Define a integer variable `mid` that is the mean of `low` and `high`. If the element at position `mid` is equal to `target`, return it. If the element is lower than `target`, shift the focus to the second half of the array by making the `low` variable equal to `mid + 1`. If the element is greater than `target` , focus on the first part of the array by making the `high` variable equal to `mid - 1`. Return `-1` as a default value if the while loop is not run.

# Complexity
- Time complexity:
$$O(log (n))$$

- Space complexity:
