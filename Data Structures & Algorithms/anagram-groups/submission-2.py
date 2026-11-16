from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # uso stringa ordinata come key!
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())
