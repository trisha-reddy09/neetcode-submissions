class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        head = 0

        slow = head
        fast = head

        # detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # find start of cycle
        ptr = head

        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return ptr