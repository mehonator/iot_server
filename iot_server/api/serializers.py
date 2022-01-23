from rest_framework import serializers

from api.models import PersonalComputer


class PersonalComputerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
        )
        model = PersonalComputer


class TelegramIDSerializer(serializers.Serializer):
    telegram_chat_id = serializers.IntegerField()


class PersonalComputerOnlyIdSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id",)
        model = PersonalComputer
