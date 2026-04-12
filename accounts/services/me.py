from accounts import models
from accounts import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class Me(ModelViewSet):
    serializer_class = serializers.MeSerializer

    def get_queryset(self):
        return models.CustomUser.objects.filter(id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)

        return Response(serializer.data)
