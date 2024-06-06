import jwt
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from django.forms.models import model_to_dict
from app.models import *
from app.serializers import *
from app.algo import *
from app.utils import *


key = "secret_key"


@api_view(["GET"])
def getUsers(request):
    users = Users.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def signUp(request):
    try:
        data = request.data
        if Users.objects.filter(email=data.get("email")).exists():
            return Response({"userAlreadyExist": True})

        hashed_password = make_password(data.get("password"))
        user = Users.objects.create(
            nom=data.get("nom"),
            prenom=data.get("prenom"),
            email=data.get("email"),
            password=hashed_password,
        )
        user.save()
        serializer = UserSerializer(user)
        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def signIn(request):
    try:
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"dataRequired": True})

        user = Users.objects.filter(email=email).first()
        if not user:
            return Response({"userNotFound": True})

        if not check_password(password, user.password):
            return Response({"incorrectPassword": True})

        token = jwt.encode(
            {
                "id": user.id,
                "exp": datetime.datetime.now(datetime.timezone.utc)
                + datetime.timedelta(days=365),
            },
            key,
            algorithm="HS256",
        )
        serializer = UserSerializer(user)
        return Response(
            {"user": serializer.data, "token": token}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def getUser(request, id):
    try:
        if not id:
            return Response({"idRequired": True})

        user = Users.objects.filter(id=id).first()

        if not user:
            return Response({"userNotFound": True})

        user_data = model_to_dict(user)

        user_data["postes"] = list(
            UserPostes.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["diplomes"] = list(
            UserDiplomes.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["formations"] = list(
            UserFormations.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["competences"] = list(
            UserCompetences.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["experiences"] = list(
            UserExperiences.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["langues"] = list(
            UserLangues.objects.filter(userId=id).values_list("value", flat=True)
        )

        return Response(
            {"user": user_data},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def editProfil(request, id):
    try:
        data = request.data

        nom = data.get("nom")
        prenom = data.get("prenom")
        telephone = data.get("telephone")
        biographie = data.get("biographie")
        pays = data.get("pays")
        region = data.get("region")
        ville = data.get("ville")
        # image = data.get("image")
        postes = data.get("postes")
        qualites = data.get("qualites")
        diplomes = data.get("diplomes")
        competences = data.get("competences")
        experiences = data.get("experiences")
        formations = data.get("formations")
        langues = data.get("langues")

        if not id:
            return Response({"idRequired": True})

        user = Users.objects.filter(id=id).first()
        if not user:
            return Response({"userNotFound": True})

        if postes:
            allItems = UserPostes.objects.filter(userId=id)
            newItemsSet = set(postes)

            if allItems.exists():
                allValues = {item.value: item for item in allItems}
                allValuesSet = set(allValues.keys())

                itemsToDelete = allValuesSet - newItemsSet
                itemsToAdd = newItemsSet - allValuesSet

                if itemsToDelete:
                    UserPostes.objects.filter(
                        userId=id, value__in=itemsToDelete
                    ).delete()

                for item in itemsToAdd:
                    UserPostes.objects.create(userId=user, value=item)

            else:
                for item in newItemsSet:
                    UserPostes.objects.create(userId=user, value=item)

        if diplomes:
            allItems = UserDiplomes.objects.filter(userId=id)
            newItemsSet = set(diplomes)

            if allItems.exists():
                allValues = {item.value: item for item in allItems}
                allValuesSet = set(allValues.keys())

                itemsToDelete = allValuesSet - newItemsSet
                itemsToAdd = newItemsSet - allValuesSet

                if itemsToDelete:
                    UserDiplomes.objects.filter(
                        userId=id, value__in=itemsToDelete
                    ).delete()

                for item in itemsToAdd:
                    UserDiplomes.objects.create(userId=user, value=item)

            else:
                for item in newItemsSet:
                    UserDiplomes.objects.create(userId=user, value=item)

        if competences:
            allItems = UserCompetences.objects.filter(userId=id)
            newItemsSet = set(competences)

            if allItems.exists():
                allValues = {item.value: item for item in allItems}
                allValuesSet = set(allValues.keys())

                itemsToDelete = allValuesSet - newItemsSet
                itemsToAdd = newItemsSet - allValuesSet

                if itemsToDelete:
                    UserCompetences.objects.filter(
                        userId=id, value__in=itemsToDelete
                    ).delete()

                for item in itemsToAdd:
                    UserCompetences.objects.create(userId=user, value=item)

            else:
                for item in newItemsSet:
                    UserCompetences.objects.create(userId=user, value=item)

        if experiences:
            allItems = UserExperiences.objects.filter(userId=id)
            newItemsSet = set(experiences)

            if allItems.exists():
                allValues = {item.value: item for item in allItems}
                allValuesSet = set(allValues.keys())

                itemsToDelete = allValuesSet - newItemsSet
                itemsToAdd = newItemsSet - allValuesSet

                if itemsToDelete:
                    UserExperiences.objects.filter(
                        userId=id, value__in=itemsToDelete
                    ).delete()

                for item in itemsToAdd:
                    UserExperiences.objects.create(userId=user, value=item)

            else:
                for item in newItemsSet:
                    UserExperiences.objects.create(userId=user, value=item)

        if formations:
            allItems = UserFormations.objects.filter(userId=id)
            newItemsSet = set(formations)

            if allItems.exists():
                allValues = {item.value: item for item in allItems}
                allValuesSet = set(allValues.keys())

                itemsToDelete = allValuesSet - newItemsSet
                itemsToAdd = newItemsSet - allValuesSet

                if itemsToDelete:
                    UserFormations.objects.filter(
                        userId=id, value__in=itemsToDelete
                    ).delete()

                for item in itemsToAdd:
                    UserFormations.objects.create(userId=user, value=item)

            else:
                for item in newItemsSet:
                    UserFormations.objects.create(userId=user, value=item)

        if qualites:
            allItems = UserQualites.objects.filter(userId=id)
            newItemsSet = set(qualites)

            if allItems.exists():
                allValues = {item.value: item for item in allItems}
                allValuesSet = set(allValues.keys())

                itemsToDelete = allValuesSet - newItemsSet
                itemsToAdd = newItemsSet - allValuesSet

                if itemsToDelete:
                    UserQualites.objects.filter(
                        userId=id, value__in=itemsToDelete
                    ).delete()

                for item in itemsToAdd:
                    UserQualites.objects.create(userId=user, value=item)

            else:
                for item in newItemsSet:
                    UserQualites.objects.create(userId=user, value=item)

        if langues:
            allItems = UserLangues.objects.filter(userId=id)
            newItemsSet = set(langues)

            if allItems.exists():
                allValues = {item.value: item for item in allItems}
                allValuesSet = set(allValues.keys())

                itemsToDelete = allValuesSet - newItemsSet
                itemsToAdd = newItemsSet - allValuesSet

                if itemsToDelete:
                    UserLangues.objects.filter(
                        userId=id, value__in=itemsToDelete
                    ).delete()

                for item in itemsToAdd:
                    UserLangues.objects.create(userId=user, value=item)

            else:
                for item in newItemsSet:
                    UserLangues.objects.create(userId=user, value=item)

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
        # if "image" in request.FILES:
        #     image = request.FILES["image"]
        #     ext = image.name.split(".")[-1]
        #     new_filename = f"{user.id}.{ext}"
        #     user.image.save(new_filename, image)
        #     user.image = f"/media/images/{new_filename}"

        user.save()
        user_data = model_to_dict(user)

        user_data["postes"] = list(
            UserPostes.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["qualites"] = list(
            UserQualites.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["diplomes"] = list(
            UserDiplomes.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["competences"] = list(
            UserCompetences.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["experiences"] = list(
            UserExperiences.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["formations"] = list(
            UserFormations.objects.filter(userId=id).values_list("value", flat=True)
        )
        user_data["langues"] = list(
            UserLangues.objects.filter(userId=id).values_list("value", flat=True)
        )

        return Response(
            {"user": user_data},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def createPoste(request, id):
    try:
        if not id:
            return Response({"idRequired": True})
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response({"userNotFound": True})

        data = request.data
        poste_data = {}
        poste_data["userId"] = user

        if "titre" in data and data["titre"]:
            poste_data["titre"] = data["titre"]
        if "telephone" in data and data["telephone"]:
            poste_data["telephone"] = data["telephone"]
        if "pays" in data and data["pays"]:
            poste_data["pays"] = data["pays"]
        if "region" in data and data["region"]:
            poste_data["region"] = data["region"]
        if "ville" in data and data["ville"]:
            poste_data["ville"] = data["ville"]
        if "description" in data and data["description"]:
            poste_data["description"] = data["description"]

        poste = Postes.objects.create(**poste_data)
        poste.save()

        missions = data.get("missions")
        langues = data.get("langues")
        competences = data.get("competences")
        experiences = data.get("experiences")
        diplomes = data.get("diplomes")
        formations = data.get("formations")
        qualites = data.get("qualites")

        if missions:
            newItemsSet = set(missions)
            for item in newItemsSet:
                PosteMissions.objects.create(posteId=poste, value=item)

        if langues:
            newItemsSet = set(langues)
            for item in newItemsSet:
                PosteLangues.objects.create(posteId=poste, value=item)

        if competences:
            newItemsSet = set(competences)
            for item in newItemsSet:
                PosteCompetences.objects.create(posteId=poste, value=item)

        if experiences:
            newItemsSet = set(experiences)
            for item in newItemsSet:
                PosteExperiences.objects.create(posteId=poste, value=item)

        if diplomes:
            newItemsSet = set(diplomes)
            for item in newItemsSet:
                PosteDiplomes.objects.create(posteId=poste, value=item)

        if formations:
            newItemsSet = set(formations)
            for item in newItemsSet:
                PosteFormations.objects.create(posteId=poste, value=item)

        if qualites:
            newItemsSet = set(qualites)
            for item in newItemsSet:
                PosteQualites.objects.create(posteId=poste, value=item)

        poste_data = model_to_dict(poste)

        poste_data["missions"] = list(
            PosteMissions.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["langues"] = list(
            PosteLangues.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["competences"] = list(
            PosteCompetences.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["experiences"] = list(
            PosteExperiences.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["diplomes"] = list(
            PosteDiplomes.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["formations"] = list(
            PosteFormations.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["qualites"] = list(
            PosteMissions.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )

        return Response(
            {"poste": poste_data},
            status=status.HTTP_201_CREATED,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def getAllPostes(request, id):
    try:
        if not id:
            return Response({"idRequired": True})
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response({"userNotFound": True})

        postes = Postes.objects.filter(userId=user.id, isDeleted=False).order_by(
            "-updatedAt"
        )
        result = []

        for poste in postes:
            poste_data = model_to_dict(poste)

            poste_data["missions"] = list(
                PosteMissions.objects.filter(posteId=poste.id).values_list(
                    "value", flat=True
                )
            )
            poste_data["langues"] = list(
                PosteLangues.objects.filter(posteId=poste.id).values_list(
                    "value", flat=True
                )
            )
            poste_data["competences"] = list(
                PosteCompetences.objects.filter(posteId=poste.id).values_list(
                    "value", flat=True
                )
            )
            poste_data["experiences"] = list(
                PosteExperiences.objects.filter(posteId=poste.id).values_list(
                    "value", flat=True
                )
            )
            poste_data["diplomes"] = list(
                PosteDiplomes.objects.filter(posteId=poste.id).values_list(
                    "value", flat=True
                )
            )
            poste_data["formations"] = list(
                PosteFormations.objects.filter(posteId=poste.id).values_list(
                    "value", flat=True
                )
            )
            poste_data["qualites"] = list(
                PosteQualites.objects.filter(posteId=poste.id).values_list(
                    "value", flat=True
                )
            )

            result.append(poste_data)

        return Response({"postes": result}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def editPoste(request, id, pk):
    try:
        if not id:
            return Response({"userIdRequired": True})
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response({"userNotFound": True})

        if not pk:
            return Response({"posteIdRequired": True})
        poste = Postes.objects.filter(id=pk, isDeleted=False).first()

        if not poste:
            return Response({"posteNotFound": True})

        data = request.data

        if "telephone" in data and data["telephone"] is not None:
            poste.telephone = data["telephone"]
        if "pays" in data and data["pays"] is not None:
            poste.pays = data["pays"]
        if "region" in data and data["region"] is not None:
            poste.region = data["region"]
        if "ville" in data and data["ville"] is not None:
            poste.ville = data["ville"]
        if "description" in data and data["description"] is not None:
            poste.description = data["description"]

        poste.save()

        def update_related(model, poste_id, values):
            model.objects.filter(posteId=poste_id).delete()
            for value in values:
                model.objects.create(posteId=poste, value=value)

        if "missions" in data:
            update_related(PosteMissions, poste.id, data.get("missions", []))
        if "langues" in data:
            update_related(PosteLangues, poste.id, data.get("langues", []))
        if "competences" in data:
            update_related(PosteCompetences, poste.id, data.get("competences", []))
        if "experiences" in data:
            update_related(PosteExperiences, poste.id, data.get("experiences", []))
        if "formations" in data:
            update_related(PosteFormations, poste.id, data.get("formations", []))
        if "diplomes" in data:
            update_related(PosteDiplomes, poste.id, data.get("diplomes", []))
        if "qualites" in data:
            update_related(PosteQualites, poste.id, data.get("qualites", []))

        poste_data = model_to_dict(poste)

        poste_data["missions"] = list(
            PosteMissions.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["competences"] = list(
            PosteCompetences.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["langues"] = list(
            PosteLangues.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["experiences"] = list(
            PosteExperiences.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["diplomes"] = list(
            PosteDiplomes.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["formations"] = list(
            PosteFormations.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )
        poste_data["qualites"] = list(
            PosteQualites.objects.filter(posteId=poste.id).values_list(
                "value", flat=True
            )
        )

        return Response(
            {"poste": poste_data},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def removePoste(request, id, pk):
    try:
        if not id:
            return Response({"userIdRequired": True})
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response({"userNotFound": True})

        if not pk:
            return Response({"posteIdRequired": True})
        poste = Postes.objects.filter(id=pk, isDeleted=False).first()

        if not poste:
            return Response({"posteNotFound": True})

        poste.isDeleted = True
        poste.save()

        poste_data = model_to_dict(poste)

        return Response(
            {"poste": poste_data},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def matchPoste(request, id, pk):
    try:
        if not id:
            return Response({"userIdRequired": True})
        user = Users.objects.filter(id=id).first()

        if not user:
            return Response({"userNotFound": True})

        if not pk:
            return Response({"posteIdRequired": True})
        poste = Postes.objects.filter(id=pk, isDeleted=False).first()

        if not poste:
            return Response({"posteNotFound": True})

        poste_data = PosteInfo(poste)
        user_data = UserInfo(user)

        result = compute_similarity(job=poste_data, profile=user_data)

        titre_score = round(result["details"]["titre"], 3)
        global_score = round(result["global_score"], 3)
        competences_score = round(result["details"]["competences"], 3)
        diplomes_score = round(result["details"]["diplomes"], 3)
        experiences_score = round(result["details"]["experiences"], 3)
        qualites_score = round(result["details"]["qualites"], 3)

        match, created = MatchResult.objects.update_or_create(
            posteId=poste,
            userId=user,
            defaults={
                "titre": titre_score,
                "globalScore": global_score,
                "competences": competences_score,
                "diplomes": diplomes_score,
                "experiences": experiences_score,
                "qualites": qualites_score,
            },
        )

        match_result = MatchResultSerializer(match)

        return Response(
            {"match": match_result.data},
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def verifyToken(request, token):
    try:
        decodedToken = jwt.decode(token, key, algorithms="HS256")
        user_id = decodedToken.get("id")

        if not user_id:
            return Response({"invalidToken": True})

        user = Users.objects.filter(id=user_id).first()
        if not user:
            return Response({"userNotFound": True})

        return Response({"decodedToken": decodedToken}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
