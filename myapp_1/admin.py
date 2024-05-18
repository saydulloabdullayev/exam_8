from django.contrib import admin

from .models import (
    TUITSystemsModel,
    TUITGroupsModel,
    TUITTypesModel,
)

# Register your models here.
admin.site.register(TUITSystemsModel)
admin.site.register(TUITGroupsModel)
admin.site.register(TUITTypesModel)
