from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(r'computers', ComputersViewSet, basename='computers')
router.register(r'monitors', MonitorsViewSet, basename='monitors')
router.register(r'softwares', SoftwaresViewSet, basename='softwares')
