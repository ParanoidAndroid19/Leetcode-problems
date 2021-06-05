
prices = [7,2,5,3,1,8]
minPrice = 10**4
maxProfit = 0

for i in range(0, len(prices)):
    if(prices[0] < minPrice):
        minPrice = prices[0]
    
    elif(prices[0] - minPrice > maxProfit):
        maxProfit = prices[0] - minPrice
    
print(maxProfit)