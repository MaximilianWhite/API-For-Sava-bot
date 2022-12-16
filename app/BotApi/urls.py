from django.urls import path, include

from .views import *

urlpatterns = [
    path('api/bot/getusersbot/<str:type>/<str:search>/', GetUsersApi.as_view()),
    path('api/bot/updatehtmlfiles', StartGetParse),
]