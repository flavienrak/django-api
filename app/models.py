from django.db import models

# Create your models here.

class Users(models.Model):
  id = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=50, null=False, default="")
  prenom = models.CharField(max_length=50, null=False, default="")
  age = models.IntegerField(null=True)
  sexe = models.CharField(max_length=5, null=True)
  etatCivil = models.CharField(max_length=10, null=True)
  adresse = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=100, unique=True, null=False, default="")
  telephone = models.CharField(max_length=25, unique=True, null=True)
  poste = models.CharField(max_length=100, null=True)
  biographie = models.CharField(max_length=250, default="")
  image=models.CharField(max_length=250, default="/user.jpg")
  password=models.CharField(max_length=250, null=False, default="")
  createdAt=models.DateTimeField(auto_created=True, null=True)
  updatedAt=models.DateTimeField(auto_created=True, null=True)
  
class Parcours(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.CharField(max_length=50, null=False)
  value = models.CharField(max_length=250, null=False)
  
class Formations(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.CharField(max_length=50, null=False)
  value = models.CharField(max_length=250, null=False)
  
class Competences(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.CharField(max_length=50, null=False)
  value = models.CharField(max_length=250, null=False)
  
class ExperiencesPro(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.CharField(max_length=50, null=False)
  value = models.CharField(max_length=250, null=False)
  
class CentreInterets(models.Model):
  id = models.AutoField(primary_key=True)
  userId = models.CharField(max_length=50, null=False)
  value = models.CharField(max_length=250, null=False)