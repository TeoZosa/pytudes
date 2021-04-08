"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Categories:
    - Array
    - Blind 75

Examples:
    >>> Solution().maxProfit([50, 30, 32, 24, 30, 40])
    16

"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return max_profit_from_stock(prices)


def max_profit_from_stock(prices: list[int]) -> int:
    """Computes the maximum possible profit from buying a single unit of stock and selling it at different day in the future

    Args:
        prices: a chronologically-ordered list of stock prices for a single stock

    Complexity:
        Time: O(n)
        Space: O(1)
    Examples:
        >>> max_profit_from_stock([])
        0
        >>> max_profit_from_stock([7,6,4,3,1])
        0
        >>> max_profit_from_stock([7,1,5,3,6,4])
        5
        >>> max_profit_from_stock([50, 30, 32, 24, 30, 40])
        16
    """
    ## EDGE CASES ##
    if not prices:
        return 0

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    min_stock_price = float("inf")
    max_profit = 0

    for stock_price in prices:
        # Track the price of the cheapest stock
        # since buying stock at that price maximizes profit when selling at any future date
        # (i.e., the delta between buy price and sell price)
        min_stock_price = min(min_stock_price, stock_price)
        # Calculate the potential profit gained if we sold `min_stock_price` today
        new_profit = stock_price - min_stock_price
        # Update `max_profit` if `new_profit` is better
        max_profit = max(max_profit, new_profit)

    return max_profit
