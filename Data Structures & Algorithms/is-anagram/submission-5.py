class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map_s = {}
        hash_map_t = {}

        for x in s:
            if x in hash_map_s:
                hash_map_s[x] = hash_map_s[x] + 1
            else:
                hash_map_s[x] = 1
        for x in t:
            if x in hash_map_t:
                hash_map_t[x] = hash_map_t[x] + 1
            else:
                hash_map_t[x] = 1

        # Comapare the two hash maps, check for equality
        if hash_map_s == hash_map_t:
            return True
        else:
            return False
        