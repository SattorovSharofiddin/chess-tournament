from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import PlayerList, GameList, UpdateRating

router = DefaultRouter()
router.register('players', PlayerList, 'players')
router.register('games', GameList, 'games')
urlpatterns = [
    path('', include(router.urls), name='index'),
    path('update-rating', UpdateRating.as_view(), name='update-rating')
]
