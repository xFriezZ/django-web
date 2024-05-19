from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('register', RegisterView.as_view(), name="register"),
]

