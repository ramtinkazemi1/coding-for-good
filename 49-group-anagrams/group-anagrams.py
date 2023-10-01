from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        for item in strs:
            key = "".join(sorted(item))
            groups[key].append(item)
        
        return groups.values()