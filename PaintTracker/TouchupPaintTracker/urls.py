from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paintList/', views.renderPaintList, name='paintList'),
    path('addNewPaint/',views.addNewPaint , name='addNewPaint'),
]