class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

     
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in hashmap:
            buckets[hashmap[num]].append(num)

        results = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num)

                if len(results) == k:
                    return results










            

        

        



        