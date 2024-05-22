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


class TUITMainModel(AbstractBaseModel):
    code = models.CharField(max_length=20, unique=True)
    system_name_uz = models.CharField(max_length=255, unique=True)
    system_name_ru = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.system_name_uz}"

    class Meta:
        db_table = 'tuit_systems'
        verbose_name_plural = 'TUIT systems'


class TUITPublicationsModel(AbstractBaseModel):
    publication_code = models.CharField(max_length=150)
    publication_name_uz = models.CharField(max_length=255)
    publication_name_ru = models.CharField(max_length=255)
    publication_system = models.ForeignKey(TUITMainModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.publication_code} - {self.publication_name_uz}"

    class Meta:
        db_table = 'tuit_publications'
        verbose_name_plural = 'TUIT publications'


class TUITPapersModel(AbstractBaseModel):
    paper_name_uz = models.CharField(max_length=100, unique=True)
    paper_name_ru = models.CharField(max_length=100, unique=True, null=True)
    paper_description_uz = models.CharField(max_length=255, null=True)
    paper_description_ru = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.paper_name_uz} - {self.paper_description_uz}"

    class Meta:
        db_table = 'tuit_papers'
        verbose_name_plural = 'TUIT papers'


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
    email = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'tuit_contacts'
        verbose_name_plural = 'TUIT Contacts'