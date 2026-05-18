class Solution:

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = n

        while True:

            slow = self.square(slow)
            fast = self.square(self.square(fast))

            if slow == fast:
                break
        return slow == 1

    def square(self, num):

        ans = 0

        while num > 0:

            digit = num % 10
            ans += digit * digit
            num //= 10

        return ans