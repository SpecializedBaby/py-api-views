from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorDetailUpdateDelete,
    ActorListCreateView,
    GenreDetail,
    GenreList,
)


router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema-halls", CinemaHallViewSet, basename="cinema-hall")

urlpatterns = [
    path("actors/", ActorListCreateView.as_view(), name="actor-list-create"),
    path(
        "actors/<int:pk>/",
        ActorDetailUpdateDelete.as_view(),
        name="actor-detail"
    ),
    path("genres/", GenreList.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
] + router.urls

app_name = "cinema"
