class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if divisor == 0:
            raise ValueError("Division by zero is undefined.")
        
        if dividend == 0:
            return 0
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        power = 31
        divisor_power = divisor << power
        
        while dividend >= divisor:
            while divisor_power > dividend:
                divisor_power >>= 1
                power -= 1
            dividend -= divisor_power
            quotient += 1 << power
        
        if negative:
            quotient = -quotient
        
        return min(max(quotient, INT_MIN), INT_MAX)
