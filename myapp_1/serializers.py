from rest_framework.serializers import ModelSerializer,SerializerMethodField
from rest_framework import serializers

from myapp_1.models import (
    TUITMainModel,
    TUITPublicationsModel,
    TUITPapersModel,
    TUITRequirementsModel,
    TUITFaqModel,
    TUITContactsModel,
)


class TUITMainSerializer(ModelSerializer):
    class Meta:
        model = TUITMainModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class TUITMainGETSerializer(ModelSerializer):
    system_name = SerializerMethodField(method_name='get_system_name', read_only=True)

    class Meta:
        model = TUITMainModel
        fields = ('id', 'code', 'system_name')

    def get_system_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.system_name_ru
            return obj.system_name_uz
        except:
            return obj.system_name_uz


class TUITPublicationsSerializer(ModelSerializer):
    class Meta:
        model = TUITPublicationsModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }


class TUITPublicationsGETSerializer(ModelSerializer):
    group_name = SerializerMethodField(method_name='get_publication_name', read_only=True)

    class Meta:
        model =TUITPublicationsModel
        fields = ('id', 'publication_code', 'group_name')

    def get_publication_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.publication_name_ru
            return obj.publication_name_uz
        except:
            return obj.publication_name_uz


class TUITPapersSerializer(ModelSerializer):
    class Meta:
        model = TUITPapersModel
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True},
        }

class TUITPapersGETSerializer(ModelSerializer):
    type_name = SerializerMethodField(method_name='get_paper_name', read_only=True)

    class Meta:
        model =TUITPapersModel
        fields = ('id', 'paper_name', 'paper_description', 'type_name')

    def get_paper_name(self, obj):
        try:
            lang = self.context['request'].GET['lang']
            if lang == 'ru':
                return obj.paper_name_ru
            return obj.paper_name_uz
        except:
            return obj.paper_name_uz
        

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
        