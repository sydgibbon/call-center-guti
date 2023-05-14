from django.urls import path

from assets.generals.views import LoginView
from . import routers
from assets.computers import views as ComputerViews

urlpatterns = [
    path('login/', LoginView.as_view())
    ]+routers.router.urls