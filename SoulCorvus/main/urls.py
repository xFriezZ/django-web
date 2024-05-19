from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('chatgpt', views.chatgpt, name='chatgpt'),
    path('telegram', views.telegram, name='telegram'),
]