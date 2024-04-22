from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload', views.fileupload, name = "File_Uploads"),
    path('process', views.process, name = "process"),
    path('delete', views.delete, name = "delete"),
]
