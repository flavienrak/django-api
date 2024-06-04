from rest_framework import serializers
from app.models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=Users
    fields=('id', 'nom', 'prenom', 'pays', 'region', 'ville', 'email', 'telephone', 'biographie', 'image', 'createdAt', 'updatedAt')

class PosteSerializer(serializers.ModelSerializer):
  class Meta:
    model=Postes
    fields="__all__"