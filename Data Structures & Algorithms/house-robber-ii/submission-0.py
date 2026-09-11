# TECNICA: in caso circolare, in cui sono correlati
# conviene spezzare in due sottoproblemi nel punto in cui si legano
# attenzione a considerare anche nums[0] separato
# dato che 1: e :-1 funzionano SSE ho almeno 2 case, con una resta vuoto!
class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], # caso in cui ho un solo elemento
                    self.robNeighborhood(nums[1:]),     # tutto tranne primo
                    self.robNeighborhood(nums[:-1]))    # tutto tranne ultimo

    def robNeighborhood(self, nums):    # uguale a House Robber I
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2