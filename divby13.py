# Algorithm: Check if a large number (given as a string) is divisible by 13
# -------------------------------------------------------------------------
# Problem: You are given a number `s` in string format which may be too large 
# to convert into an integer directly. You need to determine if it is divisible by 13.
#
# Idea:
# Instead of converting the whole string into an integer, simulate the modulo operation
# digit-by-digit (like long division). We maintain a running `remainder` and at each step:
#
#   remainder = (remainder * 10 + int(current_digit)) % 13
#
# This ensures we never build the full number, but we correctly compute its mod 13.
# If the final remainder is 0 → it is divisible by 13.

class Solution:
    def divby13(self, s: str) -> bool:
        remainder = 0
        for digit in s:
            remainder = (remainder * 10 + int(digit)) % 13
        return remainder == 0
