from posixpath import basename
from django.urls import path
from .views import *
from . import routers

urlpatterns = [
    path('computers/', ComputersViewSet.as_view({'get': 'list'}), name='computers_list'),
    ]+routers.router.urls