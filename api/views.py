from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote

# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# @api_view(['POST',"GET"])
# def signUp(request):
#     data = request.data
#     user = User.objects.all()
#     newUser = User.objects.create(
#         fname = data["fname"],
#         email = data["email"],
#         password = data["password"],
#     )
#     serializer = UserSerializer(user, many=True)
#     return Response(serializer.data)
    #user = User.objects.get(email = )
    

@api_view(["GET","POST"])
def getNotes(request):
    if request.method=="GET":
        return getNotesList(request)
    elif request.method=="POST":
        return createNote(request)

@api_view(["GET","PUT","DELETE","POST"])
def getNote(request,pk):
    if request.method=="GET":
        return getNoteDetail(request,pk)
    elif request.method=="PUT":
        return updateNote(request,pk)
    elif request.method=="DELETE":
        return deleteNote(request,pk)
    elif request.method=="POST":
        return createNote(request)
        
# @api_view(['GET'])
# def getNotes(request):
#     notes = Note.objects.all()
#     serializers = NoteSerializer(notes, many=True)
#     notesData = serializers.data
#     return Response(notesData)

# @api_view(["GET"])
# def getNote(request,pk):
#     note = Note.objects.get(id=pk)
#     serializers = NoteSerializer(note,many=False)
#     noteData = serializers.data
#     return Response(noteData)

# @api_view(["PUT"])
# def updateNote(request,pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance = note,data=data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(["DELETE"])
# def deleteNote(request,pk):
#     note = Note.objects.get(id = pk)
#     note.delete()
#     return Response("Successfully Deleted")

# @api_view(["POST"])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer= NoteSerializer(note,many=False)
#     return Response(serializer.data)