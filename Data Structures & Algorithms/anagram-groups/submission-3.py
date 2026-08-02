class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_map = {}
        for s in strs:
            sorted_text = sorted(s)
            myseperator = ""
            x = myseperator.join(sorted_text)
            if x in hash_map:
                hash_map[x].append(s)
            else:
                hash_map[x] = [s]
        for x in hash_map:
            result.append(hash_map[x])
        return result
        