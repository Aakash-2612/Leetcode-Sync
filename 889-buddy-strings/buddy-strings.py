class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        d1 = Counter(s)
        d2 = Counter(goal)
        if len(s) != len(goal):
            return False
        if s == goal:
            for i in d1:
                if d1[i] >= 2:
                    return True
            return False
        else:
            if d1 != d2:
                return False
            else:
                arr = [i for i in s]
                flag = False
                temp = '0'
                count = 0
                for i in range(len(arr)):
                    if arr[i] != goal[i]:
                        if not flag:
                            temp = arr[i]
                            arr[i] = goal[i]
                            flag = True
                        else:
                            arr[i] = temp
                        count += 1
                        if count == 2:
                            break
                return ''.join(arr) == goal

                        