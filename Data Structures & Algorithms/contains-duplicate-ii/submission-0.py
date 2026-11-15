class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1 2 3 1
        # {1: [0, 3]
        #  2: [1]
        #  3: [2]}
        # poi itero su ogni lista e vedo se c'è un delta < k
        # sono già ordinate, ez
        counter = defaultdict(list)
        for idx, num in enumerate(nums):
            counter[num].append(idx)
        
        for num in counter.keys():
            if len(counter[num]) > 1:
                for i in range(1, len(counter[num])):
                    if counter[num][i] - counter[num][i-1] <= k:
                        return True

        return False