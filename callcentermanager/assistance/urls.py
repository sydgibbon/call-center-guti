from django.urls import path
from .views import *
from . import routers

urlpatterns = [

    ]+routers.router.urls