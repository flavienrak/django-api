from rest_framework import serializers
from app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "id",
            "nom",
            "prenom",
            "pays",
            "region",
            "ville",
            "email",
            "telephone",
            "biographie",
            "image",
            "createdAt",
            "updatedAt",
        )


class MatchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchResult
        fields = "__all__"
