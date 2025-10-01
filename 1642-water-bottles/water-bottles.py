class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles >= numExchange:
            count += numBottles//numExchange
            rem = numBottles % numExchange
            numBottles = rem + (numBottles//numExchange)

        return count