redShirtHeights = [19, 2, 4, 6, 2, 3, 1, 1, 4]
blueShirtHeights = [21, 5, 4, 4, 4, 4, 4, 4, 4]

def classPhotos(redShirtHeights, blueShirtHeights):
    photoable = True
    redShirtHeights.sort()
    blueShirtHeights.sort()
    print("Red: :",redShirtHeights)
    print("Blue: :",blueShirtHeights)
    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            photoable = redShirtHeights[i] < blueShirtHeights[i]
            if photoable is False:
                return photoable
    else:
        for i in range(len(redShirtHeights)):
            photoable = redShirtHeights[i] > blueShirtHeights[i]
            if photoable is False:
                return photoable
    return photoable

answer = classPhotos(redShirtHeights, blueShirtHeights)
print("Final answer: ", answer)
