class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counter = Counter(nums)
        # i = 0
        # # items per coppia key-value
        # for letter, occurrences in sorted(counter.items()):
        #     for j in range(occurrences):
        #         nums[i+j] = letter
        #     i = i + occurrences
        

        # sfrutto che ci sono solo 3 colori
        occurrences = [0, 0, 0]

        for n in nums:
            occurrences[n] += 1

        counter = 0
        for i in range(3):
            for _ in range(occurrences[i]):
                nums[counter] = i
                counter += 1






