def findClosestValueInBst(tree, target):
    return closest(tree, target, float('inf'))

def closest(node, target, currentClosest):
    print("Node value: ",node.value)
    print("Current Closest: ",currentClosest)
    if node is None:
        return currentClosest
        
    if node.value == target:
        currentClosest = node.value
        return currentClosest
        
    print("Difference:",currentClosest," versus ",node.value, "which is closer to ",target)
    
    if abs(node.value - target) < abs(currentClosest - target):
        currentClosest = node.value
        print("New current closest: ",currentClosest)
        
    if node.value > target:
        print("Going left")
        if node.left is None:
            return currentClosest
        else:
            return closest(node.left, target, currentClosest)
    elif node.value < target:
        print("Going right")
        if node.right is None:
            return currentClosest
        else:
            return closest(node.right, target, currentClosest)
    return currentClosest
    
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Notes from Friday below

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_bst_from_dict(tree_data):
    node_map = {}
    
    # Create nodes and store them in a dictionary for easy reference
    for node_data in tree_data["tree"]["nodes"]:
        node = BST(node_data["value"])
        node_map[node_data["id"]] = node

    # Connect nodes based on left and right references
    for node_data in tree_data["tree"]["nodes"]:
        node = node_map[node_data["id"]]
        node.left = node_map.get(node_data["left"])
        node.right = node_map.get(node_data["right"])

    # Return the root node
    return node_map[tree_data["tree"]["root"]]

def print_bst_nodes(root):
    if root is not None:
        # print(f"Node: {root.value}, Left: {root.left.value if root.left else None}, Right: {root.right.value if root.right else None}")
        print_bst_nodes(root.left)
        print_bst_nodes(root.right)

# Example usage:
tree_data = {
    "target": 29751,
    "tree": {
        "nodes": [
            {"id": "100", "left": "5", "right": "502", "value": 100},
            {"id": "502", "left": "204", "right": "55000", "value": 502},
            {"id": "55000", "left": "1001", "right": None, "value": 55000},
            {"id": "1001", "left": None, "right": "4500", "value": 1001},
            {"id": "4500", "left": None, "right": None, "value": 4500},
            {"id": "204", "left": "203", "right": "205", "value": 204},
            {"id": "205", "left": None, "right": "207", "value": 205},
            {"id": "207", "left": "206", "right": "208", "value": 207},
            {"id": "208", "left": None, "right": None, "value": 208},
            {"id": "206", "left": None, "right": None, "value": 206},
            {"id": "203", "left": None, "right": None, "value": 203},
            {"id": "5", "left": "2", "right": "15", "value": 5},
            {"id": "15", "left": "5-2", "right": "22", "value": 15},
            {"id": "22", "left": None, "right": "57", "value": 22},
            {"id": "57", "left": None, "right": "60", "value": 57},
            {"id": "60", "left": None, "right": None, "value": 60},
            {"id": "5-2", "left": None, "right": None, "value": 5},
            {"id": "2", "left": "1", "right": "3", "value": 2},
            {"id": "3", "left": None, "right": None, "value": 3},
            {"id": "1", "left": "-51", "right": "1-2", "value": 1},
            {"id": "1-2", "left": None, "right": "1-3", "value": 1},
            {"id": "1-3", "left": None, "right": "1-4", "value": 1},
            {"id": "1-4", "left": None, "right": "1-5", "value": 1},
            {"id": "1-5", "left": None, "right": None, "value": 1},
            {"id": "-51", "left": "-403", "right": None, "value": -51},
            {"id": "-403", "left": None, "right": None, "value": -403}
        ],
        "root": "100"
    }
}

# Build the BST object from the provided data
bst_root = build_bst_from_dict(tree_data)

# Print all nodes in the BST
print_bst_nodes(bst_root)

print(bst_root.right.value)

def findClosestValueInBst(bst_root, target,currentClosestId = bst_root.value):
    if bst_root == None:
        return currentClosestId

    if head_node == None:
       head_node = next(node for node in tree["nodes"] if node["id"] == tree["root"])
    currentClosestId = head_node["id"]
    print("head_node[value] is ",head_node["value"])
    print("Current node is: ",head_node)
    print("Current distance up top is ",currentClosestId)
    if head_node["value"] == target:
        return currentClosestId
    elif head_node["value"] > target:
        print("Going left")
        if abs(target - head_node["value"]) < currentDistance:
            currentDistance = abs(target - head_node["value"])
            print("Current distance changed to ",currentClosestId)
        if head_node["left"] == None:
            return currentClosestId
        return findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["left"]))
    else:
        print("Going right")
        if abs(target - head_node["value"]) < currentDistance:
            currentDistance = abs(target - head_node["value"])
            print("Current distance changed to ",currentClosestId)
        if head_node["right"] == None:
            return currentClosestId
        return findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["right"]))
    

answer = findClosestValueInBst(tree, target)
print(answer)


# target = 29751
# tree = {
#   "nodes": [
#       {"id": "100", "left": "5", "right": "502", "value": 100},
#       {"id": "502", "left": "204", "right": "55000", "value": 502},
#       {"id": "55000", "left": "1001", "right": None, "value": 55000},
#       {"id": "1001", "left": None, "right": "4500", "value": 1001},
#       {"id": "4500", "left": None, "right": None, "value": 4500},
#       {"id": "204", "left": "203", "right": "205", "value": 204},
#       {"id": "205", "left": None, "right": "207", "value": 205},
#       {"id": "207", "left": "206", "right": "208", "value": 207},
#       {"id": "208", "left": None, "right": None, "value": 208},
#       {"id": "206", "left": None, "right": None, "value": 206},
#       {"id": "203", "left": None, "right": None, "value": 203},
#       {"id": "5", "left": "2", "right": "15", "value": 5},
#       {"id": "15", "left": "5-2", "right": "22", "value": 15},
#       {"id": "22", "left": None, "right": "57", "value": 22},
#       {"id": "57", "left": None, "right": "60", "value": 57},
#       {"id": "60", "left": None, "right": None, "value": 60},
#       {"id": "5-2", "left": None, "right": None, "value": 5},
#       {"id": "2", "left": "1", "right": "3", "value": 2},
#       {"id": "3", "left": None, "right": None, "value": 3},
#       {"id": "1", "left": "-51", "right": "1-2", "value": 1},
#       {"id": "1-2", "left": None, "right": "1-3", "value": 1},
#       {"id": "1-3", "left": None, "right": "1-4", "value": 1},
#       {"id": "1-4", "left": None, "right": "1-5", "value": 1},
#       {"id": "1-5", "left": None, "right": None, "value": 1},
#       {"id": "-51", "left": "-403", "right": None, "value": -51},
#       {"id": "-403", "left": None, "right": None, "value": -403}
#     ],
#   "root": "100"
# }

# Okay so I'm getting an error on Algo because I practiced with a dictionary (tree) instead of a BST but the concept and approach to solving it was right!

# 

# def findClosestValueInBst(tree, target, head_node = None):
#     if head_node == None:
#        head_node = next(node for node in tree["nodes"] if node["id"] == tree["root"])
#     currentClosestId = head_node["id"]
#     print("head_node[value] is ",head_node["value"])
#     print("Current node is: ",head_node)
#     print("Current distance up top is ",currentClosestId)
#     if head_node["value"] == target:
#         return currentClosestId
#     elif head_node["value"] > target:
#         print("Going left")
#         if abs(target - head_node["value"]) < currentDistance:
#             currentDistance = abs(target - head_node["value"])
#             print("Current distance changed to ",currentClosestId)
#         if head_node["left"] == None:
#             return currentClosestId
#         return findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["left"]))
#     else:
#         print("Going right")
#         if abs(target - head_node["value"]) < currentDistance:
#             currentDistance = abs(target - head_node["value"])
#             print("Current distance changed to ",currentClosestId)
#         if head_node["right"] == None:
#             return currentClosestId
#         return findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["right"]))
    

# answer = findClosestValueInBst(tree, target)
# print(answer)

# # One function to find the root node and determine if there is one
# headId = tree["root"]
# head_node = next(node for node in tree["nodes"] if node["id"] == headId)
# print("Head Node:", head_node)

# def findClosestValueInBst(tree, target,head_node):
#     currentClosestId = head_node["id"]
#     currentDistance = abs(target - head_node["value"])
#     print("Current closest node is ",currentClosestId)
#     print("Current distance is ",currentDistance)
#     #One function going down
#     if head_node == None:
#         return None
#     elif head_node["value"] == target:
#         return currentClosestId
#     elif head_node["value"] > target:
#         # go left
#         print("We are going to the left here")
#         print("Our new head_node is: ",head_node)
#         if abs(target - head_node["value"]) < currentDistance:
#             currentDistance = abs(target - head_node["value"])
#             print("There's a new currentDistance in town: ",currentDistance)
#         if head_node["left"] == None:
#             print("No node to the left. We found our answer. currentClosestId is: ",currentClosestId)
#             return currentClosestId
            
#         findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["left"]))
#     else:
#         # go right
#         print("We are going to the right here")
#         print("Our new head_node is: ",head_node)
#         if abs(target - head_node["value"]) < currentDistance:
#             currentDistance = abs(target - head_node["value"])
#             print("RIGHT: There's a new currentDistance in town: ",currentDistance)
#         if head_node["right"] == None:
#             print("No node to the right. We found our answer. currentClosestId is: ",currentClosestId)
#             return currentClosestId
            
#         findClosestValueInBst(tree, target,head_node = next(node for node in tree["nodes"] if node["id"] == head_node["right"]))



