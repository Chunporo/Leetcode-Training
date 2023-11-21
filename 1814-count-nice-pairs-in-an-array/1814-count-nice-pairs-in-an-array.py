class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int(str(num)[::-1])

        counter = {}
        for num in nums:
            counter[num - rev(num)] = counter.get(num - rev(num), 0) + 1

        res = 0
        for freq in counter.values():
            res += freq * (freq - 1) // 2

        return res % (10**9 + 7)