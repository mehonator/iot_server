from rest_framework.views import APIView
from rest_framework.response import Response
from wakeonlan import send_magic_packet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from api.models import PersonalComputer
from api.serializers import (
    PersonalComputerSerializer,
    TelegramIDSerializer,
)


class ListView(mixins.ListModelMixin, GenericViewSet):
    pass


class PersonalCompueterListView(ListView):
    queryset = PersonalComputer.objects.all()
    serializer_class = PersonalComputerSerializer


class WakeOnLan(APIView):
    def post(self, request, id):
        if not PersonalComputer.objects.filter(id=id).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        telegram_id_serializer = TelegramIDSerializer(data=request.data)
        if not telegram_id_serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=telegram_id_serializer.errors,
            )

        computer = PersonalComputer.objects.get(id=id)
        telegram_chat_id = telegram_id_serializer.validated_data[
            "telegram_chat_id"
        ]
        if not computer.allowed_profiles.filter(
            telegram_user_id=telegram_chat_id
        ).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)

        pc_serializer = PersonalComputerSerializer(computer)
        data = pc_serializer.data
        data["message"] = "Turn On signal has sended"
        send_magic_packet(computer.mac_address)
        return Response(
            status=status.HTTP_200_OK,
        )
