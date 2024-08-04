from django.urls import path
from . import views
urlpatterns = [
    path('',views.inherit,name='inherit'),
    path('create/',views.create,name='create'),
    path('list/',views.list,name='list'),
    path('edit/',views.edit,name='edit')
]
