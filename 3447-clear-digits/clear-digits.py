class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        index = -1
        if s.isalpha():
            return s
        else:
            for i in range(len(s) - 1, -1, -1):
                # print(index)
                if s[i].isdigit():
                    stack.append([s[i], True])
                    index += 1
                elif index != -1:
                    if stack[index][1] == True:
                        stack.pop()
                        index -= 1
                        # print(index)
                    else:
                        stack.append([s[i], False])
                        index += 1
                else:
                    stack.append([s[i], False])
                    index += 1
                # print(stack)

            my = ''
            for i in stack:
                my += i[0]
            return my[::-1]