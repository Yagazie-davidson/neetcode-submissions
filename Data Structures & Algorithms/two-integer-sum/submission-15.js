class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        if(nums.length >= 2){
            const hash = {};
            for (let i = 0; i<nums.length; i++){
                hash[nums[i]] = i;
            }
            for(let j = 0; j<nums.length; j++){
                let difference = target - nums[j]
                if(hash[difference] != undefined && hash[difference] != j){
                    return [j, hash[difference]]
                }
            }
            
                
        }

    }
}
