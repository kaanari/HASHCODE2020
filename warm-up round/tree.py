import sys
sys.setrecursionlimit(1000000)


import fileop
from collections import Counter

Leaves = []
nums = []

class Node:
    def __init__(self,data,del_numbers = 0, height = 0, parent = 0):
        self.data = data
        self.child = []
        self.deleted_numbers = del_numbers
        self.height = height
        self.parent = parent

    def addChild(self,newNode):
        self.child.append(newNode)


class AKTree:
    def __init__(self,MaxSlice, TypeNumbers, Array):
        self.root = Node(sum(Array)-MaxSlice)
        self.MaxSlice = MaxSlice
        self.Array = Array
        self.TypeNumbers = TypeNumbers


def recursion(currentNode):
    global Leaves
    global nums
    currentHeight = currentNode.height
    nextHeight = currentHeight + 1
    currentData = currentNode.data
    deleted = []
    if currentHeight >= 1:
        tempNode = currentNode
        deleted = []
        for i in range(currentHeight):
            deleted.append(tempNode.deleted_numbers)
            tempNode = tempNode.parent

    for num in Array:
        if num in deleted:
            continue

        if currentData-num == 0:
            tempNode = currentNode
            result = deleted
            result.append(num)
            return result

        elif currentData-num < 0:
            newNode = Node(currentData - num, num, nextHeight, currentNode)
            #currentNode.child.append(newNode)
            Leaves.append(newNode)

            return False

        newNode = Node(currentData-num,num,nextHeight,currentNode)
        currentNode.child.append(newNode)
        try:
            result = recursion(newNode)
        except RecursionError:
            return False

        if result:
            return result




filename = "e_also_big.in"
Input = fileop.read_file(filename)
MaxSlice, TypeNumbers, Array = fileop.split_file(Input)


Tree = AKTree(MaxSlice,TypeNumbers,Array)

currentNode = Tree.root
result = recursion(currentNode)
#print(result)
if result:
    Result = list((Counter(Array) - Counter(result)).elements())

    for i in range(len(Result)):
        Result[i] = Array.index(Result[i])
        Array[Result[i]] = -1


    #print(len(Result))

    #print(*Result)

else:

    x = []
    for i in Leaves:
        x.append(i.data)

    diff = -1000000000000
    id = 0
    inx = 0

    for i in x:

        if diff < i:
            diff = i
            inx = id

        id += 1

    node = Leaves[inx]
    height = node.height
    result = []
    for i in range(height):
        result.append(node.deleted_numbers)
        node = node.parent

    Result = list((Counter(Array) - Counter(result)).elements())
    for i in range(len(Result)):
        Result[i] = Array.index(Result[i])
        Array[Result[i]] = -1


    #print(len(Result))

    #print(*Result)

filename = filename[:-2]
filename = filename+"out"
f = open(filename, "w")
listToStr = ' '.join(map(str, Result))

f.write(str(len(Result))+"\n"+listToStr)

f.close()
