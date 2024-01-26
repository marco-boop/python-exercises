coins = [87]

# //messy 

# def nonConstructibleChange(coins):
#     theChange = 1
#     if len(coins) == 0:
#         return theChange
#     if len(coins) == 1:
#         if coins[0] == 1:
#             theChange = 2
#         else:
#             theChange = 1
#         return theChange
#     sortedCoins = sorted(coins)
#     print(sortedCoins)
#     sumOfSmallCoins = 0
#     for coin in range(len(sortedCoins)-1):
#         print("index is currently: ", coin)
#         sumOfSmallCoins += sortedCoins[coin]
#         print("The sum of small coins is ",sumOfSmallCoins)
#         nextLargestCoin = sortedCoins[coin + 1]
#         print("The value of the next largest coint is ",nextLargestCoin)
#         if sumOfSmallCoins + 1 < nextLargestCoin:
#             print("Value of theChange updated to sumofsmallcounts plus 1:", sumOfSmallCoins + 1)
#             theChange = sumOfSmallCoins + 1
#             return theChange
#         else:
#             print("If you see this, it means that sumofSmall is equal or larger than the next coin")
#             # theChange = sumOfSmallCoins + 1
#             # print("At this point theChange is now ", theChange)
#         theChange = sumOfSmallCoins + nextLargestCoin + 1
#     return theChange

def nonConstructibleChange(coins):
    # Define our placeholder
    theChange = 1
    sumOfSmallCoins = 0
    # Then all the exceptions for small array
    if len(coins) == 0:
        return theChange
    if len(coins) == 1:
        if coins[0] == 1:
            theChange = 2
        else:
            theChange = 1
        return theChange
    # Sort the existing array
    sortedCoins = sorted(coins)
    for coin in range(len(sortedCoins)-1):
        sumOfSmallCoins += sortedCoins[coin]
        nextLargestCoin = sortedCoins[coin + 1]
        if sumOfSmallCoins + 1 < nextLargestCoin:
           sumOfSmallCoins + 1
           theChange = sumOfSmallCoins + 1
           return theChange
        theChange = sumOfSmallCoins + nextLargestCoin + 1
    return theChange


answer = nonConstructibleChange(coins)
print(answer)