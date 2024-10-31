https://leetcode.com/problems/jump-game/description/
55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        far=0
        for i in range(0,n):
            if(i>far):
                return False
            far=max(far,i+nums[i])  
        return True     
