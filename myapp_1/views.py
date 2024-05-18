from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import TUITGroupsFilter
from .models import (
    TUITSystemsModel,
    TUITGroupsModel,
    TUITTypesModel,
)
from .permissions import IsSuperUserORReadOnly
from .serializers import (
    TUITSystemsSerializer, TUITSystemsGETSerializer,
    TUITGroupsSerializer, TUITGroupsGETSerializer,
    TUITTypesSerializer,
)


# Create your views here.
class TUITSystemsViewSet(ModelViewSet):
    queryset = TUITSystemsModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TUITSystemsGETSerializer
        return TUITSystemsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save

class TUITGroupsViewSet(ModelViewSet):
    queryset = TUITGroupsModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TUITGroupsFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TUITGroupsGETSerializer
        return TUITGroupsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return serializer.save


class TUITTypesViewSet(ModelViewSet):
    queryset = TUITTypesModel.objects.all()
    permission_classes = [IsSuperUserORReadOnly]
    serializer_class = TUITTypesSerializer


