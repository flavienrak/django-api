from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Users
from rest_framework import status
from app.serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
import jwt
import datetime

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
          createdAt=timezone.now(),
          updatedAt=timezone.now()
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
      
    return Response({ "decodedToken": decodedToken }, status=status.HTTP_200_OK)
  except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      