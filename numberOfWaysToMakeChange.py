n = 6
denoms = [1, 5]

def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n + 1)
    pointer = 0
    while pointer < len(denoms):
        for i in range(len(ways)):
            if pointer == 0 and i == 0:
                ways[i] += 1
            if denoms[pointer] <= i:
                ways[i] += ways[i - denoms[pointer]]
        pointer += 1
    print(ways[-1])

answer = numberOfWaysToMakeChange(n, denoms)
print(answer)