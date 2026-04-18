class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for val in nums:
            if val in seen:
                return True   # duplicate found
            seen.add(val)
        return False          # no duplicates