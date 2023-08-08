from unicodedata import name
from django.urls import path
from .import views

urlpatterns=[

    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('log/',views.log,name="log"),
    path('home/',views.home,name="home"),
    path('view/',views.view,name="view"),
    path('file/',views.file,name="file"),
    # path('upload/',views.upload,name="upload"),
    path('delete/<str:pk>',views.delete,name="delete")

    
]