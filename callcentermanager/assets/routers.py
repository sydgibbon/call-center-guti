from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(
    'computers', ComputersViewSet, basename='computers',
    
)
