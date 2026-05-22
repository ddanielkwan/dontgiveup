# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) 
# for which the stock price was less than or equal to the price of that day.

# For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, 
# then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
# Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8,
#  then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.
 

# Example 1:

# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6
class StockSpanner:
    #  [7,2,1,2] and the price of the stock today is 2, span is 4 
    #we would use a mono decreasing stack
    #keep track of each day, in stack how many days i am greater or equal to prev <- this is span not days case we add up and consolidate
    def __init__(self):
        #maximum number of consecutive days from that day, and going backwards
        #since we only care about consecutive smallers , can we have mono decreasing stack where we store the (price, how many days this price already covers)
        #if todays price is larger
        self.stack = [] #
    def next(self, price: int) -> int:
        
        span = 1 #span has to be ata least one because today 

        while self.stack and self.stack[-1][0] <= price: #starting from today and going backwards, get all the smaller ones
        #so at any moment, the last element of stack should be the smallest price and they already collected all of its previous smaller ones, so we just check today's
            _, prevSpan = self.stack.pop()
            span += prevSpan
        
        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

