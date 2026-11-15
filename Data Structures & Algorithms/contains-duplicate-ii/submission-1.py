'''
Sliding Window + Set
Posso usare il set con dimensione fissa come "distanza"

Con nums = [1, 2, 1] e k = 2:
- i = 0: {1}
- i = 1: {1, 2}
- i = 2: il 1 è già nel set -> True. dist è 2

Mantengo nel set gli ultimi k elementi.
Se il numero corrente è già nel set, ho trovato
un duplicato a distanza <= k.

Rimuovo l'elemento che esce dalla finestra.
O(n) time, O(k) space.
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])

        return False



'''
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
'''