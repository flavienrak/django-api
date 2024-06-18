from django.db import models

# Users.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50, null=False, default="")
    prenom = models.CharField(max_length=50, null=False, default="")
    email = models.CharField(max_length=100, unique=True, null=False, default="")
    password = models.CharField(max_length=250, null=False, default="")
    pays = models.CharField(max_length=25, null=False, default="")
    region = models.CharField(max_length=50, null=False, default="")
    ville = models.CharField(max_length=50, null=False, default="")
    telephone = models.CharField(max_length=25, null=False, default="")
    biographie = models.CharField(max_length=250, default="")
    # image = models.ImageField(upload_to="images/", blank=True, null=True)
    image = models.CharField(max_length=250, unique=True, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)


class UserPostes(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    value = models.CharField(max_length=50, null=False, default="")


class UserQualites(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class UserDiplomes(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class UserFormations(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class UserCompetences(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class UserExperiences(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class UserLangues(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    value = models.CharField(max_length=25, null=False, default="")


# Postes


class Postes(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50, null=False, default="")
    pays = models.CharField(max_length=25, null=False, default="")
    region = models.CharField(max_length=50, null=False, default="")
    ville = models.CharField(max_length=50, null=False, default="")
    telephone = models.CharField(max_length=25, null=False, default="")
    description = models.CharField(max_length=250, default="")
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)


class PosteMissions(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class PosteDiplomes(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class PosteFormations(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class PosteCompetences(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class PosteQualites(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class PosteExperiences(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=False, default="")


class PosteLangues(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    value = models.CharField(max_length=25, null=False, default="")


# Match result


class MatchResult(models.Model):
    id = models.AutoField(primary_key=True)
    posteId = models.ForeignKey(Postes, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    titre = models.DecimalField(max_digits=5, decimal_places=3)
    globalScore = models.DecimalField(max_digits=5, decimal_places=3)
    competences = models.DecimalField(max_digits=5, decimal_places=3)
    diplomes = models.DecimalField(max_digits=5, decimal_places=3)
    experiences = models.DecimalField(max_digits=5, decimal_places=3)
    qualites = models.DecimalField(max_digits=5, decimal_places=3)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)
