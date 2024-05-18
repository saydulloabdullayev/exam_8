from django.urls import path
from rest_framework import routers

from myapp_1.views import (
    TUITSystemsViewSet,
    TUITGroupsViewSet,
    TUITTypesViewSet,
)


router = routers.DefaultRouter()
router.register(r'systems', TUITSystemsViewSet, basename='system')
router.register(r'groups', TUITGroupsViewSet, basename='group')
router.register(r'types', TUITTypesViewSet, basename='type')


urlpatterns = router.urls

