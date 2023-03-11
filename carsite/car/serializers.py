from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    cena = serializers.CharField()
