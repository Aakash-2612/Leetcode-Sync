class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = k
        val = 0
        while len(s) > k:
            st = ''
            # print(f'{s = }')
            for i in range(0, len(s)):
                if count > 0:
                    count -= 1
                    val += int(s[i])
                    # print(f'{i = }')
                    # print(f'{val = }')
                else:
                    st += str(val)
                    # print(f'{st = }')
                    count = k-1
                    val = int(s[i])

            st += str(val)
            val = 0
            count = k
            # print(f'{val = }')
            # print(f'{count = }')
            s = st
            # print(st)

        return s