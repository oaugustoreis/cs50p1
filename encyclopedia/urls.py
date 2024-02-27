from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.new_page, name="newPage"),
    path("editpage/", views.edit, name="edit"),
    path("save/", views.save, name="save"),
    path("random/", views.randomContent, name="random"),
    
]
