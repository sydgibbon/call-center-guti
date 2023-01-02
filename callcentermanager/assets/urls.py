from django.urls import path
from .views import *
from . import routers

urlpatterns = [
    path('login/', LoginView.as_view()),
    ]+routers.router.urls