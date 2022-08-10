# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 1232ms 25.1MB
class Solution:
    @staticmethod
    def maxProfit(prices: list[int]) -> int:
        low_point = prices[0]
        earn = 0
        for price in prices:
            # 더 작은값 나오면 low_point 갱신
            if price < low_point:
                low_point = price
            # 더 큰이득 나오면 earn 갱신
            if earn < (price - low_point):
                earn = price - low_point
        return earn