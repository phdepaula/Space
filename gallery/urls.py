from django.urls import path
from gallery.views import index, star, galaxy, nebula, planet

urlpatterns = [
    path("", index, name="index"),
    path("star/", star, name = "star"),
    path("galaxy/", galaxy, name = "galaxy"),
    path("nebula/", nebula, name = "nebula"),
    path("planet/", planet, name = "planet"),
]
