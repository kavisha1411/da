from django.urls import path
from rest_framework import routers
from . import views

'''urlpatterns = [
	path('songlist/', views.SongApi, name='songlist'),
	# path('songdetail/<int:id>/', views.SongDetail.as_view(), name='songdetail'),
	
]'''


router = routers.DefaultRouter()
router.register("Song", views.SongApi)
router.register("Album", views.AlbumApi)
router.register("Artist", views.ArtistApi)

