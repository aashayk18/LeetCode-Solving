# Intuition
Keep track of the count of consecutive 1's by iterating over the array while using counter variables.

# Approach
Initialize two variables `count` and `max_one` to 0. Iterate over the list `nums` and if the element is 0, keep count as 0. Otherwise, if the element is 1, increase count by 1. Check if `max_one` is greater or `count`, and assign the higher value to `max_one`. Return `max_one` as the output. 

# Complexity
- Time complexity:


- Space complexity:
