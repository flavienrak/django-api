from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Users
from rest_framework import status
from app.serializers import UserSerializer
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
def getUsers(request):
  users = Users.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def signUp(request):
  try:
    data = request.data
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
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)3
      