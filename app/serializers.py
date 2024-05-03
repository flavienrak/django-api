from rest_framework import serializers
from app.models import Users

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=Users
    fields=('id', 'nom', 'prenom', 'age', 'sexe', 'etatCivil', 'adresse', 'email', 'telephone', 'poste', 'biographie', 'image', 'password', 'createdAt', 'updatedAt')