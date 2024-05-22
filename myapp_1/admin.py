from django.contrib import admin

from .models import (
    TUITMainModel,
    TUITPublicationsModel,
    TUITPapersModel,
    TUITRequirementsModel,
    TUITFaqModel,
    TUITContactsModel,
)

# Register your models here.
admin.site.register(TUITMainModel)
admin.site.register(TUITPublicationsModel)
admin.site.register(TUITPapersModel)
admin.site.register(TUITRequirementsModel)
admin.site.register(TUITFaqModel)
admin.site.register(TUITContactsModel)