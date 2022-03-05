from minimaxsumgame.serializers import MinimaxPackSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from minimaxsumgame.serializers import MinimaxPackSerializer

class GetMinimaxResponse(GenericAPIView):
    serializer_class = MinimaxPackSerializer

    def get(self, request): 
        ins = request.GET.getlist('inputs')
        
        return Response(ins)