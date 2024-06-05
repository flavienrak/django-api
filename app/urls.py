from django.urls import path
from . import views

urlpatterns = [
    path("sign-up", views.signUp, name="sign-up"),
    path("sign-in", views.signIn, name="sign-in"),
    path("get-users/", views.getUsers, name="get-users"),
    path("user/<str:id>/get-user", views.getUser, name="get-user"),
    path("user/<str:id>/edit-profil", views.editProfil, name="edit-profil"),
    path("user/<str:id>/create-poste", views.createPoste, name="create-poste"),
    path("user/<str:id>/poste/get-all", views.getAllPostes, name="get-all-postes"),
    path("user/<str:id>/poste/<str:pk>/edit-poste", views.editPoste, name="edit-poste"),
    path(
        "user/<str:id>/poste/<str:pk>/remove-poste",
        views.removePoste,
        name="remove-poste",
    ),
    path(
        "user/<str:id>/poste/<str:pk>/match-result",
        views.matchPoste,
        name="match-poste",
    ),
    path("verify-token/<str:token>", views.verifyToken, name="verify-token"),
]
