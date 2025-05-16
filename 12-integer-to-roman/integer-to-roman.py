class Solution:
    def cal(self, val, symbols, s, my, zero_count):
        n = int(str(val)[:1])
        if n == 0:
            return s[::-1]
        if n == 1:
            s += symbols[int(str(my[n]) + ('0'*zero_count))]
            # print(s)
            return s[::-1]
        
        s += symbols[int(str(my[n]) + ('0'*zero_count))]
        # print(s)
        if n == 4 or n == 9:
            n = 1
        else:
            n -= my[n]
        return self.cal(n, symbols, s, my, zero_count)

    def intToRoman(self, num: int) -> str:
        symbols = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        my = {
            1: 1,
            2: 1,
            3: 1,
            4: 5,
            5: 5,
            6: 5,
            7: 5,
            8: 5,
            9: 10
        }
        zero_count = -1
        ans = []
        for i in reversed(str(num)):
            zero_count += 1
            val = int(i + ('0' * zero_count))
            if i != '0':
                res = self.cal(val, symbols, '', my, zero_count)
                if i == '4' or i == '9':
                    ans.append(res)
                else:
                    ans.append(res[::-1])
            # print(ans)
        
        return ''.join(i for i in ans[::-1])