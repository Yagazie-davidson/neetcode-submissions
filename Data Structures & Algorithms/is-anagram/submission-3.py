class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashMapS[s[i]] = 1 + hashMapS.get(s[i], 0)
            hashMapT[t[i]] = 1 + hashMapT.get(t[i], 0)
        
        for j in hashMapS:
            if hashMapS[j] != hashMapT.get(j, 0):
                return False
            
        return True
            

