class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        pre_sums, d, sum = [0], defaultdict(list), 0
        for n in nums:
            sum += n
            pre_sums.append(sum)
        for i, v in enumerate(pre_sums):
            d[v].append(i)
        for j in range(1, len(nums) - 1):
            for k in range(j+1, len(nums) - 1):
                last_sum = pre_sums[-1] - pre_sums[k+1]
                for i in d[last_sum]:
                    if i >= j:
                        break
                    if pre_sums[i] == pre_sums[j] - pre_sums[i+1] == pre_sums[k] - pre_sums[j+1]:
                        return True
        return False

'''
presum: P[i] = P[j] - P[i+1] = P[k] - P[j+1] = P[-1] - P[k+1]
1. find P[i] == P[-1] - P[k+1]
2. check if i < j
3. check the rest equation P[i] = P[j] - P[i+1] = P[k] - P[j+1]  
'''