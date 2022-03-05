

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

    
    