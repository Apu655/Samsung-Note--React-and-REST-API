from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes,name="GetRoutes"),
    path("notes/",views.getNotes, name="GetNotes"),
    #path("notes/create",views.createNote,name="CreateNote"),
    #path("notes/<str:pk>/update",views.updateNote, name="UpdateNote"),
    #path("notes/<str:pk>/delete",views.deleteNote, name="DeleteNote"),
    path("notes/<str:pk>",views.getNote, name="GetNote"),
    
]