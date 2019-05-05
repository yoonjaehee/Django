from django.urls import path
from .views import documentlist , createDocument , documentdetail, updateDocument, deleteDocument
urlpatterns = [
    path('', documentlist, name="documentlist"),
    path('<int:id>/' , documentdetail, name="detailview"),
    path('create/' , createDocument, name="createDocument"),
    path('<int:id>/update/', updateDocument, name="updateDocument"),
    path('<int:id>/delete/', deleteDocument, name="deleteDocument"),
]