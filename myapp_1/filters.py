import django_filters

from .models import TUITGroupsModel


class TUITGroupsFilter(django_filters.FilterSet):
    group_system = django_filters.CharFilter(lookup_expr='exact', required=True)

    class Meta:
        model = TUITGroupsModel
        fields = ['group_system']