from rest_framework.serializers import ModelSerializer,SerializerMethodField

from myapp_1.models import (
    TUITSystemsModel,
    TUITGroupsModel,
    TUITTypesModel,
)


class TUITSystemsSerializer(ModelSerializer):
    class Meta:
        model = TUITSystemsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class TUITSystemsGETSerializer(ModelSerializer):
    system_name = SerializerMethodField(method_name='get_system_name', read_only=True)

    class Meta:
        model = TUITSystemsModel
        fields = ('id', 'code', 'system_name')

    def get_system_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.system_name_ru
            return obj.system_name_uz
        except:
            return obj.system_name_uz


class TUITGroupsSerializer(ModelSerializer):
    class Meta:
        model = TUITGroupsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class TUITGroupsGETSerializer(ModelSerializer):
    group_name = SerializerMethodField(method_name='get_group_name', read_only=True)

    class Meta:
        model =TUITGroupsModel
        fields = ('id', 'group_code', 'group_name')

    def get_group_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.group_name_ru
            return obj.group_name_uz
        except:
            return obj.group_name_uz


class TUITTypesSerializer(ModelSerializer):
    class Meta:
        model = TUITTypesModel
        fields = '__all__'
