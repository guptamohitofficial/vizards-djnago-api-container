from card.models import *
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class ShortCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['bname','id','timeMeeting']