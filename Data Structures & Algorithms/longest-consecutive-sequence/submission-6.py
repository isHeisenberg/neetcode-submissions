class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        length = len(nums)
        if length == 0:
            return 0

        sort = sorted(nums)
        maxlen = 1

        for i in range(length):
            counter = 1
            for j in range(i + 1, length):
                if sort[j] == sort[j - 1]:
                    continue
                if sort[j] == sort[j - 1] + 1:
                    counter += 1
                else:
                    break

            maxlen = max(maxlen, counter)  # ✅ fondamentale

        return maxlen