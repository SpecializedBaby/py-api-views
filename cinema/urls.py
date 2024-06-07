from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorList,
    ActorDetail,
    GenreDetail,
    GenreList,
)


router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema-hall")

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list-create"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
] + router.urls

app_name = "cinema"
