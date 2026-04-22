class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True   # duplicate found
            hashset.add(n)
        return False          # no duplicates