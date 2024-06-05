from app.models import *


class PosteInfo:
    def __init__(self, poste):
        self.titre = poste.titre
        self.competences = list(
            PosteCompetences.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        self.langues = list(
            PosteLangues.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        self.experiences = list(
            PosteExperiences.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        self.diplomes = list(
            PosteDiplomes.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        self.formations = list(
            PosteFormations.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        self.qualites = list(
            PosteQualites.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )


class UserInfo:
    def __init__(self, user):
        self.postes = list(
            UserPostes.objects.filter(userId=user.id).values_list("value", flat=True)
        )
        self.qualites = list(
            UserQualites.objects.filter(userId=user.id).values_list("value", flat=True)
        )
        self.diplomes = list(
            UserDiplomes.objects.filter(userId=user.id).values_list("value", flat=True)
        )
        self.competences = list(
            UserCompetences.objects.filter(userId=user.id).values_list(
                "value", flat=True
            )
        )
        self.experiences = list(
            UserExperiences.objects.filter(userId=user.id).values_list(
                "value", flat=True
            )
        )
        self.formations = list(
            UserFormations.objects.filter(userId=user.id).values_list(
                "value", flat=True
            )
        )
        self.langues = list(
            UserLangues.objects.filter(userId=user.id).values_list("value", flat=True)
        )
