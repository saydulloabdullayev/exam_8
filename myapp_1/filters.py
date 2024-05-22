import django_filters

from .models import TUITPublicationsModel


class TUITPublicationsFilter(django_filters.FilterSet):
    publications_system = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = TUITPublicationsModel
        fields = ['publications_system']