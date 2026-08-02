class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = list()

        for n in nums:
            if n in hashset:
                return True
            hashset.append(n)
        return False
    