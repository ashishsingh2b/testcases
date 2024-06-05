from django.urls import path
from .views import NoteListCreate,NoteListRetrive

urlpatterns = [
    path('notes/', NoteListCreate.as_view(), name='note-list-create'),
    path('notesrud/<int:pk>/',NoteListRetrive.as_view(), name='note-list-retrive'),
]
