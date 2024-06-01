from rest_framework import serializers
from app.models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=Users
    fields=('id', 'nom', 'prenom', 'pays', 'region', 'ville', 'email', 'telephone', 'biographie', 'image', 'createdAt', 'updatedAt')

class Titres(serializers.ModelSerializer):
  class Meta:
    model=Titres
    fields="__all__"

class Diplomes(serializers.ModelSerializer):
  class Meta:
    model=Diplomes
    fields="__all__"

class Formations(serializers.ModelSerializer):
  class Meta:
    model=Formations
    fields="__all__"

class Competences(serializers.ModelSerializer):
  class Meta:
    model=Competences
    fields="__all__"

class Experiences(serializers.ModelSerializer):
  class Meta:
    model=Experiences
    fields="__all__"

class Langues(serializers.ModelSerializer):
  class Meta:
    model=Langues
    fields="__all__"

class Postes(serializers.ModelSerializer):
  class Meta:
    model=Postes
    fields="__all__"