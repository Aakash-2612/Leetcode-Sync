class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        # print(penalty)
        ans = -1
        min_ans = float("inf")
        if penalty < min_ans:
            min_ans = penalty
            ans = 0
        for ind, i in enumerate(customers):
            if i == 'Y':
                penalty -= 1
                if penalty < min_ans:
                    min_ans = penalty
                    ans = ind+1
            else:
                penalty += 1
        
        return ans