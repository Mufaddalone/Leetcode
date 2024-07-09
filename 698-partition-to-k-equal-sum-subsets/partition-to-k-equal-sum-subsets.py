class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k
        nums.sort(reverse=True)  # Sort in descending order for better pruning
        used = [False] * len(nums)
        
        def backtrack(start, k, current_sum):
            if k == 0:
                return True
            if current_sum == target_sum:
                return backtrack(0, k - 1, 0)
            for i in range(start, len(nums)):
                if not used[i] and current_sum + nums[i] <= target_sum:
                    used[i] = True
                    if backtrack(i + 1, k, current_sum + nums[i]):
                        return True
                    used[i] = False
                    if current_sum == 0:
                        return False
            return False
        
        return backtrack(0, k, 0)