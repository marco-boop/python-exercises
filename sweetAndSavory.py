# dishes = [-3, -5, 1, 7]
# target = 8
# dishes = [3,5,7,2,6,8,1]
# target = 10
# dishes = [2,5,-4,-7,12,100,-25]
# target = -20
dishes = [-5, 10]
target = 4

# missing: the dish can't be more savory than target

def sweetAndSavory(dishes, target):
    dishes.sort()
    sweetPoint = 0
    savoryPoint = len(dishes) - 1
    bestBet = float("inf")
    winningDuo = [0, 0]
    if len(dishes) < 2 or dishes[sweetPoint] > 0 or dishes[savoryPoint] < 0:
        return winningDuo
    while dishes[sweetPoint] < 0 and dishes[savoryPoint] > 0:
        currentSum = dishes[sweetPoint] + dishes[savoryPoint]
        currentDistance = abs(target - currentSum)
        print(currentSum)
        if currentSum == target:
            return [dishes[sweetPoint], dishes[savoryPoint]]
        elif currentSum > target:
            savoryPoint -= 1
        else:       
            if currentDistance < bestBet:
                bestBet = currentDistance
                winningDuo = [dishes[sweetPoint], dishes[savoryPoint]]
            sweetPoint += 1

    return winningDuo
        
    

answer = sweetAndSavory(dishes, target)
print(answer)