from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter

from .filters import TUITGroupsFilter
from .models import (
    TUITSystemsModel,
    TUITGroupsModel,
    TUITTypesModel,
    TUITRequirementsModel,
    TUITFaqModel,
    TUITContactsModel,
)
from .permissions import IsSuperUserORReadOnly
from .serializers import (
    TUITSystemsSerializer, TUITSystemsGETSerializer,
    TUITGroupsSerializer, TUITGroupsGETSerializer,
    TUITTypesSerializer,
    TUITRequirementsSerializer,
    TUITFAQSerializer,
    TUITContactsSerializer,
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



class TUITRequirementsViewSet(ModelViewSet):
    queryset = TUITRequirementsModel.objects.all()
    serializer_class = TUITRequirementsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['req_title_uz', 'req_title_ru']
    search_fields = ['req_title_uz','req_title_ru', 'req_description_uz','req_description_ru']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TUITRequirementsSerializer
        return TUITRequirementsSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        return serializer.save


class TUITFAQViewSet(ModelViewSet):
    queryset = TUITFaqModel.objects.all()
    serializer_class = TUITFAQSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['question_uz', 'question_ru']
    search_fields = ['question_uz','question_ru', 'answer_uz', 'answer_ru']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TUITFAQSerializer
        return TUITFAQSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        return serializer.save


class TUITContactsViewSet(viewsets.ModelViewSet):
    queryset = TUITContactsModel.objects.all()
    serializer_class = TUITContactsSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'message']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TUITContactsSerializer
        return TUITContactsSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        return serializer.save