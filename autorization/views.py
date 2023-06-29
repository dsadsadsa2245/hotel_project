from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from . import serializers
# from account.send_mail import
from rest_framework.response import Response

User = get_user_model()


class UserViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

    @action(['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=201)

    @action(['GET'], detail=False)
    def get_all_users(self, request):
        # Получаем queryset модели User
        serializer = serializers.get_serializer(queryset, many=True)  # Сериализуем queryset
        return Response(serializer.data)





