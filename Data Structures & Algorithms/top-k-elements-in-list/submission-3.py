class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums).most_common(k)
        res = []
        for i in freq:
            res.append(i[0])
        return res