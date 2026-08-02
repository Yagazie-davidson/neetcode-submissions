class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length != t.length) return false;
        const hash1 = {};
        const hash2 = {};
        for(let i = 0; i < s.length; i++){
            if(s[i] in hash1){
                hash1[s[i]] = hash1[s[i]] + 1
            }else{
                hash1[s[i]] = 1
            }
        }
        for(let j = 0; j < t.length; j++){
            if(t[j] in hash2){
                hash2[t[j]] = hash2[t[j]] + 1
            }else{
                hash2[t[j]] = 1
            }
        }
        for (const key in hash1){
            if (hash1[key] !== hash2[key]){
                return false
            }
        }
        
        return true
    }
}
