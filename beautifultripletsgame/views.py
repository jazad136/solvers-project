from django.shortcuts import render
from django.http import JsonResponse

from beautifultripletsgame.service import beautriplets_service
# Create your views here.

def index(request):
    inputs = request.GET.get('inputs')
    difference = request.GET.get('difference')
    intIns = []
    diffIns = []
    checkResponse = checkInputs(inputs, difference, intIns, diffIns)
    if checkResponse:
        return checkResponse
    diffIn = diffIns[0]
    sortedIns = sorted(intIns)

    beauTotal = beautriplets_service.get_beautriplets_result(diffIn, sortedIns)
    return JsonResponse({
        'answer': 'Inputs: {}, Difference: {}, Output is: {}'.format(intIns, diffIn, beauTotal)
    })

def checkInputs(inputs, difference, intIns, diffIns):
    if not inputs or len(inputs) == 0:
        return JsonResponse({
            'answer': 'No Input List Specified: Please enter ?inputs=<numbers> after the final slash in the URL'
        })
    if not difference:
        return JsonResponse({
            'answer': 'No Difference Specified: Please enter ?difference=<number> after the final slash in the URL'
        })
    ins = inputs.split(',')
    outs = []
    beautriplets_service.removeNull(ins, outs)
    if len(ins) == 0:
        return JsonResponse({
            'answer': 'Empty Input List Specified: Please enter ?inputs=<numbers> after the final slash in the URL'
        })
    inputCheck = beautriplets_service.checkAndGetInts(ins, intIns, difference, diffIns)
    if inputCheck == 'noInput':
        return JsonResponse({
            'answer': 'No Input: Please enter ?inputs=<numbers> after the final slash in the URL'
        })
    elif inputCheck == 'badInput':
        return JsonResponse({
            'answer': 'Only integers are allowed to exist in the input'
        })
    return None

def show(request):
    return render(request, 'beautifultripletsgame/home.html', {})


    
