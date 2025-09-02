from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        help_text="The number to be converted to English words"
    )