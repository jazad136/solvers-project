from rest_framework import serializers
from minimaxsumgame.models import MinimaxPack

class MinimaxPackSerializer(serializers.ModelSerializer):
    inputs = serializers.CharField(max_length=200)
    answer = serializers.Charfield(max_length=200)
    class Meta:
        model = MinimaxPack
        fields = ('inputs', 'answer')