from rest_framework import serializers

from us_fuels.models import UsFuel, USCity


class UsFuelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk')

    class Meta:
        model = UsFuel
        fields = ('id', 'fuel', 'date')


class UsCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = USCity
        fields = ('name',)
