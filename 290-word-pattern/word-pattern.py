class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        
        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}
        # pattern_to_word: {'a': 'dog', 'b': 'cat'}
        # word_to_pattern: {'dog': 'a', 'cat': 'b'}
        # zip(patter,words) = [('a', 'dog'), ('b', 'cat'), ('b', 'cat'), ('a', 'dog')]

        for char, word in zip(pattern, words):
            if char in pattern_to_word:
                if pattern_to_word[char] != word:
                    return False
            else:
                pattern_to_word[char] = word

            if word in word_to_pattern:
                if word_to_pattern[word] != char:
                    return False
            else:
                word_to_pattern[word] = char

        return True
