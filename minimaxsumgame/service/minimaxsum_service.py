#minimaxsum_service.py

def removeNull(ins): 
    outs = []
    for st in ins:
        if len(st) == 0:
            continue
        outs.append(st)
    return outs

def checkAndGetInts(ins, outs):
    if(len(ins) == 0):
        return 'noInput'
    for st in ins:
        try:
            nextOut = int(st)
            outs.append(nextOut)
        except ValueError:
            return 'badInput'
    return 'ok'

def getMinimaxResult(listS, listL):
    return "{}, {}".format(min(listS), max(listL))
def getMinimaxArrays(arr):
    outsSmall = []
    outsLarge = []
    n = len(arr)
    selected = [False for _ in range(n)]
    for i in range(4):
        nextI = nextSmallest(arr, selected)
        outsSmall.append(arr[nextI])
        selected[nextI] = True
    
    selected = [False for _ in range(n)]
    for i in range(4):
        nextI = nextLargest(arr, selected)
        outsLarge.append(arr[nextI]);
        selected[nextI] = True
    
    return outsSmall, outsLarge

def nextLargest(arr, selected):
    largest = float('-inf')
    idx = -1
    for i in range(len(arr)):
        if(arr[i] > largest and not selected[i]):
            largest = arr[i]
            idx = i
    return idx;  
  
def nextSmallest(arr, selected):
    smallest = float('inf')
    idx = -1
    for i in range(len(arr)):
        if(arr[i] < smallest and not selected[i]):
            smallest = arr[i]
            idx = i
    return idx;    
    