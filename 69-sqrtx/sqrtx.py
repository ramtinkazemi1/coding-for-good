class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Handle small cases (0 and 1)

        left, right = 2, x // 2  # Initialize binary search range

        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid  # Exact square root found
            elif mid_squared < x:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        # When loop ends, right is the integer part of the square root
        return right