from rest_framework.routers import DefaultRouter
from administration.users import views as users
from administration.entities import views as entities

router=DefaultRouter()
router.register(r'getUsers', users.GetUsersViewSet, basename='getUsers')
router.register(r'getEntitiesTable', entities.GetEntitiesViewSet, basename='getEntitiesTable')
