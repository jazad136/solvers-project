'''
TESTS
1)
7 3
1 2 4 5 7 8 10

Output is: 3
Triplets are: 1 4 7, 4 7 10

2) 
'''

def get_beau_total(remaining, diff, tip, left):
    if left == 0:
        return 1
    if len(remaining) == 0:
        return 0
    
    store = list(remaining)
    total = 0
    for el in remaining:
        store.pop(0)
        if el == tip + diff:
            new_tot = get_beau_total(store, diff, tip+diff, left-1)
            total += new_tot
        elif el > tip + diff:
            break

    return total

def get_beautriplets_result(diff, sorted_ins):
    total = 0
    while len(sorted_ins) > 0:
        tip = sorted_ins.pop(0)
        total += get_beau_total(sorted_ins, diff, tip, 2)
    return total

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = get_beautriplets_result(d, arr)

    print(str(result) + '\n')

def removeNull(ins, outs): 
    for st in ins:
        if len(st) == 0:
            continue
        outs.append(st)

def checkAndGetInts(ins, outs, inDiff, outDiffs):
    if(len(ins) == 0):
        return 'noInput'
    for st in ins:
        try:
            nextOut = int(st)
            outs.append(nextOut)
        except ValueError:
            return 'badInput'
    try:
        outDiff = int(inDiff)
        outDiffs.append(outDiff)
    except ValueError:
        return 'badInput'
    return 'ok'