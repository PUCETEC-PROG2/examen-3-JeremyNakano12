from django.urls import path
from . import views

app_name = "album_manager"
urlpatterns = [
    path("", views.index, name="index"),
    path("album/<int:album_id>/", views.album, name="album"),
    path("album/edit/<int:album_id>/", views.edit_album, name="edit_album"),
    path("album/delete/<int:album_id>/", views.delete_album, name="delete_album"),
    path("album/add_album/", views.add_album, name="add_album"),
    path("artist/<int:artist_id>/", views.artist, name="artist"),
    path("artist/add_artist/", views.add_artist, name="add_artist"),
    path("artist/edit/<int:artist_id>/", views.edit_artist, name="edit_artist"),
    path("artist/delete/<int:artist_id>/", views.delete_artist, name="delete_artist"),
    path("album/", views.list_album, name="list_album"),
    path("artist/", views.list_artist, name="list_artist"),

]