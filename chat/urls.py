from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getmessages/<str:room>/', views.getmessages, name='getmessages'),
    path('rest', views.TestApi.as_view()),
    path('api/token/', obtain_auth_token)
]