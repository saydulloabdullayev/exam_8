from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        abstract = True
        db_table = 'abstract_model'

class TUITSystemsModel(AbstractBaseModel):
    code = models.CharField(max_length=20, unique=True)
    system_name_uz = models.CharField(max_length=255, unique=True)
    system_name_ru = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.system_name_uz}"

    class Meta:
        db_table = 'tuit_systems'
        verbose_name_plural = 'TUIT systems'

class TUITGroupsModel(AbstractBaseModel):
    group_code = models.CharField(max_length=150)
    group_name_uz = models.CharField(max_length=255)
    group_name_ru = models.CharField(max_length=255)
    group_system = models.ForeignKey(TUITSystemsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group_code} - {self.group_name_uz}"

    class Meta:
        db_table = 'tuit_groups'
        verbose_name_plural = 'TUIT groups'

class TUITTypesModel(AbstractBaseModel):
    type_name_uz = models.CharField(max_length=100, unique=True)
    type_name_ru = models.CharField(max_length=100, unique=True, null=True)
    type_description_uz = models.CharField(max_length=255, null=True)
    type_description_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.type_name_uz} - {self.type_description_uz}"

    class Meta:
        db_table = 'tuit_types'
        verbose_name_plural = 'TUIT types'

class TUITRequirementsModel(AbstractBaseModel):
    req_title_uz = models.CharField(max_length=100, unique=True)
    req_title_ru = models.CharField(max_length=100, unique=True, null=True)
    req_description_uz = models.CharField(max_length=255, null=True)
    req_description_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.req_title_uz} - {self.req_description_uz}"

    class Meta:
        db_table = 'tuit_requirements'
        verbose_name_plural = 'TUIT requirements'

class TUITFaqModel(AbstractBaseModel):
    question_uz = models.CharField(max_length=100, unique=True)
    question_ru = models.CharField(max_length=100, unique=True, null=True)
    answer_uz = models.CharField(max_length=255, null=True)
    answer_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.question_uz} - {self.answer_ru}"

    class Meta:
        db_table = 'tuit_faq'
        verbose_name_plural = 'TUIT FAQ'


class TUITContactsModel(AbstractBaseModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'tuit_contacts'
        verbose_name_plural = 'TUIT Contacts'