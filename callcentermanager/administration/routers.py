from rest_framework.routers import DefaultRouter
from administration.users import views as users
from administration.groups import views as groups


router=DefaultRouter()
router.register(r'getUsers', users.GetUsersViewSet, basename='getUsers')
router.register(r'getGroupsSelect', groups.GetGroupsSelectViewSet, basename='getGroupsSelect')
