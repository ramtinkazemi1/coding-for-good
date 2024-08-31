class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # substring = sliding window
        # s = "abciiidef", k = 3

        left = max_vowels = current_vowel_count = 0
        vowels = ['a','e','i','o','u']


        for right in range(len(s)):

            if s[right] in vowels:
                current_vowel_count += 1

            if right - left + 1 > k:
                if s[left] in vowels:
                    current_vowel_count -= 1
                left += 1

            if right - left + 1 == k:
                max_vowels = max(max_vowels, current_vowel_count)
        
        return max_vowels