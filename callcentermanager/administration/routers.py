from rest_framework.routers import DefaultRouter
from administration.users import views as users

router=DefaultRouter()
router.register(r'getUsers', users.GetUsersViewSet, basename='getUsers')
