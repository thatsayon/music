from django.urls import path 
from . import views 

urlpatterns = [
    path('musician/', views.musician, name='Musician'),
    path('editmusician/<int:id>/', views.editmusician, name='EditM'),
    path('album/', views.album, name='Album'),
    path('editalbum/<int:id>/', views.editalbum, name='EditA'),
    path('deletealbum/<int:id>/', views.deletealbum, name='DltA'),
]