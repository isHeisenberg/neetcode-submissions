class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        n = len(nums)

        for num in nums:

            # se lo trovo, aumento il counter
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1

            # se None lo aggiungo
            elif count1 == 0:
                cand1 = num
                count1 += 1
            elif count2 == 0:
                cand2 = num
                count2 += 1
            else:
                # riduco ENTRAMBI i counter
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        # conteggio: infatti magari i candidati rimasti non sono buoni
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        res = []
        if count1 > n // 3:
            res.append(cand1)
        if count2 > n // 3:
            res.append(cand2)

        return res
                
            
            
