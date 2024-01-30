redShirtSpeeds = [3, 6, 7, 2, 1]
blueShirtSpeeds = [5, 5, 3, 9, 2]
fastest = True

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    preferredSpeed = 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse = fastest)
    for i in range(len(redShirtSpeeds)):
        if redShirtSpeeds[i] >= blueShirtSpeeds[i]:
            preferredSpeed += redShirtSpeeds[i]
        else:
            preferredSpeed += blueShirtSpeeds[i]
    return preferredSpeed

answer = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
print("Final answer: ", answer)