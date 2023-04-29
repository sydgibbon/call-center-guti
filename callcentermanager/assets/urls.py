from django.urls import path
from .views import *
from . import routers
from assets.computers import views as ComputerViews

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('getComputersDropdowns/', ComputerViews.GetComputersDropdowns.as_view())
    ]+routers.router.urls