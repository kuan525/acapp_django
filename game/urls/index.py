form django.urls import path, include
form game.views.index import index

urlpatterns = [
    path("", index, name="index")
    path("menu/", inlclude("game.urls.menu.index")),
    path("playground/", inlcude("game.urls.palyground.index")),
    path("settings/", include("game.urls.settings.index")),
]
