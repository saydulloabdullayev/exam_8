from django.urls import path
from rest_framework import routers

from myapp_1.views import (
    TUITSystemsViewSet,
    TUITGroupsViewSet,
    TUITTypesViewSet,
    TUITRequirementsViewSet,
    TUITFAQViewSet,
    TUITContactsViewSet,
)


router = routers.DefaultRouter()
router.register(r'systems', TUITSystemsViewSet, basename='system')
router.register(r'groups', TUITGroupsViewSet, basename='group')
router.register(r'types', TUITTypesViewSet, basename='type')
router.register(r'requirements', TUITRequirementsViewSet, basename='requirement')
router.register(r'faqs', TUITFAQViewSet, basename='faq')
router.register(r'contacts', TUITContactsViewSet, basename='contact')


urlpatterns = router.urls

