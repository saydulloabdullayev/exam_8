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
    code = models.CharField(max_length=2, unique=True)
    system_name_uz = models.CharField(max_length=255, unique=True)
    system_name_ru = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.system_name_uz}"

    class Meta:
        db_table = 'tuit_systems'
        verbose_name_plural = 'TUIT systems'

class TUITGroupsModel(AbstractBaseModel):
    group_code = models.CharField(max_length=15)
    group_name_uz = models.CharField(max_length=255)
    group_name_ru = models.CharField(max_length=255)
    group_system = models.ForeignKey(TUITSystemsModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group_code} - {self.group_name_uz}"

    class Meta:
        db_table = 'tuit_groups'
        verbose_name_plural = 'TUIT groups'

class TUITTypesModel(AbstractBaseModel):
    type_name_uz = models.CharField(max_length=10, unique=True)
    type_name_ru = models.CharField(max_length=10, unique=True, null=True)
    type_description_uz = models.CharField(max_length=255, null=True)
    type_description_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.type_name_uz} - {self.type_description_uz}"

    class Meta:
        db_table = 'tuit_types'
        verbose_name_plural = 'TUIT types'
