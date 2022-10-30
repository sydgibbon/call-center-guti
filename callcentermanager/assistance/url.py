from django.urls import path
from .views import *
from . import routers

urlpatterns = [
    path('changestickets/', ChangesTicketsViewSet.as_view({'get': 'list'}), name='changestickets_list'),
    ]+routers.router.urls