class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        i = 0
        # items per coppia key-value
        for letter, occurrences in sorted(counter.items()):
            for j in range(occurrences):
                nums[i+j] = letter
            i = i + occurrences
        