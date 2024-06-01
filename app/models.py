from django.db import models

# Create your models here.

class Users(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=50, null=False, default="")
  prenom = models.CharField(max_length=50, null=False, default="")
  email = models.CharField(max_length=100, unique=True, null=False, default="")
  password=models.CharField(max_length=250, null=False, default="")
  pays = models.CharField(max_length=25, null=False, default="")
  region = models.CharField(max_length=50, null=False, default="")
  ville = models.CharField(max_length=50, null=False, default="")
  telephone = models.CharField(max_length=25, unique=True, null=False, default="")
  biographie = models.CharField(max_length=250, default="")
  image=models.CharField(max_length=250, null=False, default="")
  createdAt=models.DateTimeField(auto_now_add=True, null=True)
  updatedAt=models.DateTimeField(auto_now=True, null=True)
  
class Postes(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  titre = models.CharField(max_length=50, null=False, default="")
  image=models.CharField(max_length=250, null=False, default="")
  createdAt=models.DateTimeField(auto_now_add=True, null=True)
  updatedAt=models.DateTimeField(auto_now=True, null=True)
    
class Titres(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  value = models.CharField(max_length=50, null=False, default="")

class Diplomes(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  posteId=models.ForeignKey(Postes, on_delete=models.CASCADE)
  value = models.CharField(max_length=100, null=False, default="")
  
class Formations(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  posteId=models.ForeignKey(Postes, on_delete=models.CASCADE)
  value = models.CharField(max_length=100, null=False, default="")
  
class Competences(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  posteId=models.ForeignKey(Postes, on_delete=models.CASCADE)
  value = models.CharField(max_length=100, null=False, default="")
  
class Experiences(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  posteId=models.ForeignKey(Postes, on_delete=models.CASCADE)
  value = models.CharField(max_length=100, null=False, default="")
  
class Langues(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.ForeignKey(Users, on_delete=models.CASCADE)
  posteId=models.ForeignKey(Postes, on_delete=models.CASCADE)
  value = models.CharField(max_length=25, null=False, default="")
  