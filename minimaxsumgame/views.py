from django.shortcuts import render
from minimaxsumgame.models import MinimaxPack
# Create your views here.
def index(request):
    context = {
        'packs': MinimaxPack.objects.all(),
    }
    return render(request, 'minimaxsumgame/inputslisting.html', context)