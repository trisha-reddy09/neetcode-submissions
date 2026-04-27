from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # sort based on frequency
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        # take first k elements
        sorted_k = sorted_items[:k]

        # return only the numbers (keys)
        result = []
        for item in sorted_k:
            result.append(item[0])

        return result

            



        