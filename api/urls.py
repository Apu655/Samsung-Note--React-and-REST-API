from django.urls import path
from . import views
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.getRoutes,name="GetRoutes"),
    path("notes/",views.getNotes, name="GetNotes"),
    #path("notes/create",views.createNote,name="CreateNote"),
    #path("notes/<str:pk>/update",views.updateNote, name="UpdateNote"),
    #path("notes/<str:pk>/delete",views.deleteNote, name="DeleteNote"),
    path("notes/<str:pk>",views.getNote, name="GetNote"),
    
]