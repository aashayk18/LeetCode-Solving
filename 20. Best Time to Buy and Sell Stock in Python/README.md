# Intuition
Traverse the array to find the minimum and maximum values for the prices of the stock.

# Approach
Initialize the max_profit variable with 0, and the min_pur variable with the first value of the array. These values represent the maximum profit and the minimum purchase price of the stock. Run a loop over the range of the 2nd value of the array to the last. Inside the loop, compare the current value of max_profit and the difference between the array element and the min_pur value. Find the greater value of the two, and assign it to the max_profit variable. This gives us the maximum profit at the current step. Compare the current value of min_pur and the array element, to find the smaller value and assign it to the min_pur variable. This gives us the minimum purchasing price at the current step. Finally, return the value of max_profit.

Over the course of the running of the loop, we identify the largest value in the array and the smallest value in the array such that after purchasing the stock at the smallest possible value we then sell it at the largest possible value. Thus, we get the maximum value out of the array which is the difference between the buying price and the selling price of the stock. 

# Complexity
- Time complexity:


- Space complexity:
