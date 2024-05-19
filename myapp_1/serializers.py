from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers

from myapp_1.models import (
    TUITSystemsModel,
    TUITGroupsModel,
    TUITTypesModel,
    TUITRequirementsModel,
    TUITFaqModel,
    TUITContactsModel,
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
        extra_kwargs = {
            'author': {'write_only': True},
        }

class TUITTypesGETSerializer(ModelSerializer):
    type_name = SerializerMethodField(method_name='get_type_name', read_only=True)

    class Meta:
        model =TUITTypesModel
        fields = ('id', 'type_name', 'type_description')

    def get_type_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.type_name_ru
            return obj.type_name_uz
        except:
            return obj.type_name_uz
        

class TUITRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUITRequirementsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class TUITRequirementsGETSerializer(ModelSerializer):
    req_title = SerializerMethodField(method_name='get_req_name', read_only=True)

    class Meta:
        model =TUITRequirementsModel
        fields = ('id', 'req_title', 'req_descriptions')

    def get_req_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.req_title_ru
            return obj.req_title_uz
        except:
            return obj.req_title_uz



class TUITFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUITFaqModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }

class TUITFAQGETSerializer(ModelSerializer):
    question = SerializerMethodField(method_name='get_question', read_only=True)

    class Meta:
        model =TUITFaqModel
        fields = ('id', 'question', 'answer')

    def get_question(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.question_ru
            return obj.question_uz
        except:
            return obj.question_uz

class TUITContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUITContactsModel
        fields = '__all__'
        