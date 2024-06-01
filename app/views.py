import jwt
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from app.models import *
from app.serializers import *

key = "secret_key"

@api_view(['GET'])
def getUsers(request):
  users = Users.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def signUp(request):
  try:
    data = request.data
    if Users.objects.filter(email=data.get("email")).exists():
        return Response({"userAlreadyExist": True})

    hashed_password = make_password(data.get('password'))
    user = Users.objects.create(
          nom=data.get('nom'),
          prenom=data.get('prenom'),
          email=data.get('email'),
          password=hashed_password,
    ) 
    user.save()
    serializer = UserSerializer(user)
    return Response({ 'user': serializer.data }, status=status.HTTP_201_CREATED)
  except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
@api_view(['POST'])
def signIn(request):
  try:
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
      return Response({"dataRequired": True})
    
    user = Users.objects.filter(email=email).first()
    if not user:
      return Response({"userNotFound": True})
    
    if not check_password(password, user.password):
      return Response({"incorrectPassword": True})
    
    token = jwt.encode({ "id": user.id, "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365) }, key, algorithm='HS256')
    serializer = UserSerializer(user)
    return Response({ 'user': serializer.data, "token": token }, status=status.HTTP_200_OK)
  except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
@api_view(['POST'])
def editProfil(request, id):
  try:
    nom = request.data.get('nom')
    prenom = request.data.get('prenom')
    telephone = request.data.get('telephone')
    biographie = request.data.get('biographie')
    pays = request.data.get('pays')
    region = request.data.get('region')
    ville = request.data.get('ville')
    image = request.data.get('image')
    titres = request.data.get('titres')
    diplomes = request.data.get('diplomes')
    competences = request.data.get('competences')
    experiences = request.data.get('experiences')
    formations = request.data.get('formations')
    langues = request.data.get('langues')

    if not id:
      return Response({"idRequired": True})
    
    user = Users.objects.filter(id=id).first()
    if not user:
      return Response({"userNotFound": True})
    
    if titres:
      allTitres = Titres.objects.filter(userId=id)
      existing_titles_dict = {titre.value: titre for titre in allTitres}

      new_titles_set = set(titres)
      existing_titles_set = set(existing_titles_dict.keys())

      titles_to_delete = existing_titles_set - new_titles_set
      titles_to_add = new_titles_set - existing_titles_set

      if titles_to_delete:
          Titres.objects.filter(userId=id, value__in=titles_to_delete).delete()

      # Ajouter les nouveaux titres
      for title in titles_to_add:
          Titres.objects.create(userId=id, value=title)
          
      # Récupérer tous les titres mis à jour pour l'utilisateur donné
      nouveauxTitres = Titres.objects.filter(userId=id).values_list('value', flat=True)
      
    if diplomes:
      allTitres = Diplomes.objects.filter(userId=id)
      existing_titles_dict = {titre.value: titre for titre in allTitres}

      new_titles_set = set(titres)
      existing_titles_set = set(existing_titles_dict.keys())

      titles_to_delete = existing_titles_set - new_titles_set
      titles_to_add = new_titles_set - existing_titles_set

      if titles_to_delete:
          Titres.objects.filter(userId=id, value__in=titles_to_delete).delete()

      # Ajouter les nouveaux titres
      for title in titles_to_add:
          Titres.objects.create(userId=id, value=title)
          
      # Récupérer tous les titres mis à jour pour l'utilisateur donné
      nouveauxTitres = Titres.objects.filter(userId=id).values_list('value', flat=True)
      
    if nom:
        user.nom = nom
    if prenom:
        user.prenom = prenom
    if telephone:
        user.telephone = telephone
    if biographie:
        user.biographie = biographie
    if pays:
        user.pays = pays
    if region:
        user.region = region
    if ville:
        user.ville = ville
    if image:
        user.image = image

    user.save()    
    
    serializer = UserSerializer(user)
    return Response({ 'user': serializer.data, 'titres': list(nouveauxTitres)}, status=status.HTTP_200_OK)
  except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
@api_view(['GET'])
def verifyToken(request, token):
  try:
    decodedToken = jwt.decode(token, key, algorithms="HS256")
    user_id = decodedToken.get("id")
        
    if not user_id:
      return Response({ "invalidToken": True })
      
    user = Users.objects.filter(id=user_id).first()
    if not user:
      return Response({"userNotFound": True})
    
    serializer = UserSerializer(user)
      
    return Response({ "decodedToken" : decodedToken, "user" : serializer.data }, status=status.HTTP_200_OK)
  except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
      