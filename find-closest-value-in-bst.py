# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

target = 12
tree = {
  "nodes": [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": "13", "right": "22", "value": 15},
    {"id": "22", "left": None, "right": None, "value": 22},
    {"id": "13", "left": None, "right": "14", "value": 13},
    {"id": "14", "left": None, "right": None, "value": 14},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": None, "right": None, "value": 5},
    {"id": "2", "left": "1", "right": None, "value": 2},
    {"id": "1", "left": None, "right": None, "value": 1}
  ],
  "root": "10"
}

# One function to find the root node and determine if there is one
headId = tree["root"]
head_node = next(node for node in tree["nodes"] if node["id"] == headId)
print("Head Node:", head_node)

def findClosestValueInBst(tree, target,head_node):
    currentClosestId = head_node["id"]
    currentDistance = abs(target - head_node["value"])
    print("Current closes node is ",currentClosestId)
    print("Current distance is ",currentDistance)
    #One function going down
    if head_node == None:
        return None
    elif head_node["value"] == target:
        return currentClosestId
    elif head_node["value"] > target:
        # go left
        print("We are going to the left here")
        if abs(target - head_node["value"]) < currentDistance:
            currentDistance = abs(target - head_node["value"])
            print("There's a new currentDistance in town: ",currentDistance)
        if head_node["left"] == None:
            print("No node to the left. We found our answer")
            return currentClosestId
            
        findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["left"]))
    else:
        # go right
        print("We are going to the right here")
        print("Our new head_node is: ",head_node)
        if abs(target - head_node["value"]) < currentDistance:
            currentDistance = abs(target - head_node["value"])
            print("RIGHT: There's a new currentDistance in town: ",currentDistance)
        if head_node["right"] == None:
            print("No node to the right. We found our answer")
            return currentClosestId
            
        findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["right"]))

answer = findClosestValueInBst(tree, target,head_node)
print(answer)