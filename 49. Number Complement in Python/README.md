# Intuition
Convert to binary, replace 1's with 0's and vice versa. Return after converting back to decimal.

# Approach
Use the `bin()` function to convert `num` into a binary string `s` and use the `replace()` function to edit out the `'0b'` part that gets added by default to such binary string conversions. Initialize an empty string `t`. Iterate over each character in `s`, and if it is a `1` concatenate `t` with `0` and if the character is a 0 concatenate `t` with `1`. Thus, we end up with a string `t` that is a binary complement of string `s`. Convert `t` to a decimal integer using the `int()` function.

# Complexity
- Time complexity:


- Space complexity:
