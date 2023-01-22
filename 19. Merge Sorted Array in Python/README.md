# Intuition
Add the elements of second array to the end of the first array, and sort the first array.

# Approach
Initialize a count variable with 0. Run a while loop with the condition that m is less than the length of the first array nums1. Inside the loop, assign the value of the element of nums2 at the index given by count, to the element of nums1 at the index given by m i.e. the element just after the last actual element of nums1. Increment count and m by 1, and thus add the elements of nums2 to nums1 at the end. Finally, after the merging of the two arrays is done, sort the array.

# Complexity
- Time complexity:


- Space complexity:
