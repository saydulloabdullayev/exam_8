from django.urls import path
from rest_framework import routers

from myapp_1.views import (
    TUITMainViewSet,
    TUITPublicationsViewSet,
    TUITPapersViewSet,
    TUITRequirementsViewSet,
    TUITFAQViewSet,
    TUITContactsViewSet,
)


router = routers.DefaultRouter()
router.register(r'main', TUITMainViewSet, basename='Main')
router.register(r'publications', TUITPublicationsViewSet, basename='Publication')
router.register(r'papers', TUITPapersViewSet, basename='Paper')
router.register(r'requirements', TUITRequirementsViewSet, basename='Requirement')
router.register(r'faqs', TUITFAQViewSet, basename='FAQ')
router.register(r'contacts', TUITContactsViewSet, basename='Contact')


urlpatterns = router.urls

