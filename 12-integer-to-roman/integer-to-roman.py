class Solution:
    def intToRoman(self, num: int) -> str:

        #descending order by integer value
        roman_numbers = {1000: "M", 900: "CM", 500: "D", 400: "CD", 
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

        #sort ht in decreasing order if it is not sorted
        #(sorted(roman_numerals.keys(), reverse=True))

        roman = ""
        for value in roman_numbers:
            while num>=value:
                roman += roman_numbers[value]
                num -= value
        return roman