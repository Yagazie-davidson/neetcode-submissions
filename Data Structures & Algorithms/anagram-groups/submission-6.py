class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            x = "".join(sorted(s))
            res[x].append(s)
        return list(res.values())