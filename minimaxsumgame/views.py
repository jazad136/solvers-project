from django.shortcuts import render
from minimaxsumgame.models import MinimaxPack
from django.http import JsonResponse
from minimaxsumgame.service import minimaxsum_service
# Create your views here.
def index(request):
    context = {
        'packs': MinimaxPack.objects.all(),
    }
    return render(request, 'minimaxsumgame/inputslisting.html', context)

def show(request):
    inputs = request.GET.get('inputs')
    if not inputs or len(inputs) == 0:
        return JsonResponse({
            'answer': 'No Input: Please enter ?inputs=<numbers> after the final slash in the URL'
        })
    ins = inputs.split(',')
    minimaxsum_service.removeNull(ins)
    intInputs = []
    inputCheck = minimaxsum_service.checkAndGetInts(ins, intInputs)
    if inputCheck == 'noInput':
        return JsonResponse({
            'answer': 'No Input: Please enter ?inputs=<numbers> after the final slash in the URL'
        })
    elif inputCheck == 'badInput':
        return JsonResponse({
            'answer': 'Only integers are allowed to exist in the input'
        })
    
    context = {
        'pack': intInputs
    }
    return render(request, 'minimaxsumgame/inputslisting2.html', context)